import pygame
from constants import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=BLUE):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
class BadBlock(Block):
    def __init__(self, x, y, width, height, color=RED):
        super().__init__(x, y, width, height, color)
        
    def die(self):
        print("Enemy die")
