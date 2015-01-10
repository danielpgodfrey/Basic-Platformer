# Thanks to RootOfTheNull for 
import pygame

from block import Block
from constants import *
from player import Player
from level import Level01

class Platformer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.fps = 30
        
        self.set_properties()
        
    def set_properties(self):
        """Set properties inherent to this game."""        
        self.font = pygame.font.SysFont("Arial", 30)

        self.level_list = []
    
    def load_levels(self, player):
        self.level_list.append(Level01(player))
        
    def get_current_level(self, current_level_number):
        return self.level_list[current_level_number]
        
    def play(self):
        object_list = pygame.sprite.Group()
        player = Player()
        object_list.add(player)

        player.set_position(30, 30)
        
        self.load_levels(player)
        current_level_number = 0
        current_level = self.get_current_level(current_level_number)
        player.level = current_level
        #message = previous_message = None
        #self.set_message("")
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        running = False
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(
                        event.dict['size'], pygame.RESIZABLE)
                    
            player.update(current_level.platform_list, 
                current_level.enemy_list, event)
            
            current_level.update()
            
            current_level.draw(self.screen)
            object_list.draw(self.screen)
            
            self.clock.tick(self.fps)
            pygame.display.flip()
            
        pygame.quit()

#    def set_message(self, text):
#        message = self.font.render(text, True, BLACK, WHITE)
#        previous_message = message

if __name__ == "__main__":
    game = Platformer()
    game.play()
