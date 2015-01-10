import pygame
from constants import *
from block import Block, BadBlock

class Level:
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player_object = player
        
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        
    def draw(self, screen):
        screen.fill(WHITE)
        self.enemy_list.draw(screen)
        self.platform_list.draw(screen)
        
class Level01(Level):
    def __init__(self, player):
        super().__init__(player)
        platforms = [ [2, 124, 365, 47, GREEN], 
                      [200, 424, 280, 47, GREEN] ]
        
        enemies = [ [64, 100, 100, 47, RED],
                          [400, 233, 23, 47, RED] ]
                        
        
        for platform in platforms:
            block = Block(platform[0], platform[1], platform[2], platform[3], platform[4])
            self.platform_list.add(block)
            
        for enemy in enemies:
            block = BadBlock(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4])
            self.enemy_list.add(block)
