# Thanks to RootOfTheNull for 
import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color=RED, width=48, height=48):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.set_properties()
        
        self.hspeed = 0
        self.vspeed = 0
        self.level = None
        
    def set_properties(self):
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        self.speed = 5
        
    def change_speed(self, hspeed, vspeed):
        self.hspeed = hspeed
        self.vspeed = vspeed
        
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y
        
    def set_image(self, filename = None):
        if filename:
            self.image = pygame.image.load(filename)
            self.set_properties()
            
    def update(self, collidable = pygame.sprite.Group(), event = None):
        self.experience_gravity()
        self.rect.x += self.hspeed
        collision_list = pygame.sprite.spritecollide(self, collidable, False)
        
        for collided_object in collision_list:
        
            if self.hspeed > 0:
                self.rect.right = collided_object.rect.left
        
            elif self.hspeed < 0:
                self.rect.left = collided_object.rect.right
                
        self.rect.y += self.vspeed
        
        collision_list = pygame.sprite.spritecollide(self, collidable, False)
        
        for collided_object in collision_list:
            
            if self.vspeed > 0:
                self.rect.bottom = collided_object.rect.top
                self.vspeed = 0
            
            elif self.vspeed < 0:
                self.rect.top = collided_object.rect.bottom
                self.vspeed = 0
                
        if event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hspeed = -self.speed
                
                if event.key == pygame.K_RIGHT:
                    self.hspeed = self.speed
                    
                if event.key == pygame.K_UP:
                    if len(collision_list) > 0:
                        self.vspeed = -(self.speed) * 2
                
                if event.key == pygame.K_DOWN:
                    pass
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if (self.hspeed < 0):
                        self.hspeed = 0
                        
                if event.key == pygame.K_RIGHT:
                    if (self.hspeed > 0):
                        self.hspeed = 0
                        
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                    
    def experience_gravity(self, gravity = .40):
        if self.vspeed == 0:
            self.vspeed = 1
        else:
            self.vspeed += gravity

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=BLUE):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

class Level:
    def __init__(self, player):
        self.object_list = pygame.sprite.Group()
        self.player_object = player
        
    def update(self):
        self.object_list.update()
        
    def draw(self, screen):
        screen.fill(WHITE)
        self.object_list.draw(screen)
        
class Level01(Level):
    def __init__(self, player):
        super().__init__(player)
        level_blocks = [ [2, 124, 365, 47, GREEN], 
                        [200, 424, 280, 47, GREEN] ]
        
        for block in level_blocks:
            block = Block(block[0], block[1], block[2], block[3], block[4])
            self.object_list.add(block)

def set_message(text, font):
    global message, previous_message
    message = font.render(text, True, BLACK, WHITE)
    previous_message = message

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    
    clock = pygame.time.Clock()
    fps = 30
    
    object_list = pygame.sprite.Group()
    player = Player()
    player.set_position(30, 30)
    
    object_list.add(player)
    
    level_list = []
    level_list.append(Level01(player))
    
    current_level_number = 0
    current_level = level_list[current_level_number]
    player.level = current_level
    font = pygame.font.SysFont("Arial", 30)
    message = previous_message = None
    set_message("", font)
    
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                
        player.update(current_level.object_list, event)
        
        current_level.update()
        
        current_level.draw(screen)
        object_list.draw(screen)
        clock.tick(fps)
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()
