import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        
        # gernaral setup 
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        
        # player movement 
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = self.speed
        
        elif keys[pygame.K_LEFT]:
            self.direction.x = self.speed * -1
        
        else:
            self.direction.x = 0
    
    def update(self):
        self.get_input()
        self.rect.x += self.direction.x