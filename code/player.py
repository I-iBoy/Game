import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        
        # general setup 
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        
        # player movement 
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_setup = 3
        self.speed = self.speed_setup
        self.gravity = 0.8
        self.jump_speed = -16
        
        self.on_ground = False
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = self.speed
        
        elif keys[pygame.K_LEFT]:
            self.direction.x = self.speed * -1
        
        elif keys[pygame.K_SPACE] and self.on_ground:
            self.direction.y = self.jump_speed
        
        else:
            self.direction.x = 0
    
    def get_gravity(self):
        self.direction.y += self.gravity 
        self.rect.y += self.direction.y
    
    def update(self):
        self.get_input()
        self.rect.x += self.direction.x