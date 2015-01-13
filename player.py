import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color=BLUE, width=48, height=48):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.set_properties()
        
        self.hspeed = 0
        self.vspeed = 0
        self.speed = 5
        self.jump_speed = 10
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
            
    def update(self, platforms = pygame.sprite.Group(), 
        enemies = pygame.sprite.Group(), event = None):
        # Handle x position
        self.rect.x += self.hspeed
        platforms_list = pygame.sprite.spritecollide(self, platforms, False)
        for collided_object in platforms_list:
            self.collide_x(collided_object)
        
        # Handle y position
        self.experience_gravity()
        self.rect.y += self.vspeed
        platforms_list = pygame.sprite.spritecollide(self, platforms, False)
        for collided_object in platforms_list:
            self.collide_y(collided_object)
                
        collided_enemy_list = pygame.sprite.spritecollide(self, enemies, False)
        for collided_enemy in collided_enemy_list:
            self.collide_enemies_x(collided_enemy)
        
        collided_enemy_list = pygame.sprite.spritecollide(self, enemies, False)
        for collided_enemy in collided_enemy_list:
            self.collide_enemies_y(collided_enemy)
            
        if event:
            self.controls(event, platforms_list)

    def controls(self, event, collision_list):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left()
            
            if event.key == pygame.K_RIGHT:
                self.move_right()
                
            if event.key == pygame.K_UP:
                if len(collision_list) > 0:
                    self.jump()
                    
            if event.key == pygame.K_DOWN:
                pass
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if (self.hspeed < 0):
                    self.stop_horizontal()
                    
            if event.key == pygame.K_RIGHT:
                if (self.hspeed > 0):
                    self.stop_horizontal()
                    
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

    def collide_enemies_x(self, collided_enemy):
        pass
            
    def collide_enemies_y(self, collided_enemy):
        # Going up
        if self.rect.centery < collided_enemy.rect.centery:
            self.change_speed(0, -self.jump_speed*2)
            collided_enemy.die()
            
        # Going down
        elif self.rect.centery > collided_enemy.rect.centery:
            self.collide_y(collided_enemy)
            self.die()
            
    def collide_x(self, collided_object):
        """Handle horizontal collisions for the player"""
        if self.hspeed > 0:
            self.rect.right = collided_object.rect.left
    
        elif self.hspeed < 0:
            self.rect.left = collided_object.rect.right
            
    def collide_y(self, collided_object):
        """Handle vertical collisions for the player"""
        if self.vspeed > 0:
            self.rect.bottom = collided_object.rect.top
            self.vspeed = 0
        
        elif self.vspeed < 0:
            self.rect.top = collided_object.rect.bottom
            self.vspeed = 0
                
    def experience_gravity(self, gravity = .40):
        if self.vspeed == 0:
            self.vspeed = 1
        else:
            self.vspeed += gravity
    
    def move_left(self):
        self.hspeed = -self.speed
        
    def move_right(self):
        self.hspeed = self.speed
        
    def stop_horizontal(self):
        self.hspeed = 0
    
    def jump(self):
        self.vspeed = -self.jump_speed
        
    def die(self):
        print("Player die")
