import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
    
    def update(self, x_shift):
        self.rect.x = x_shift