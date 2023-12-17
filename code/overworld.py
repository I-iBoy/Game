import pygame
from support import import_folder
from setting import screen_height, screen_width

class Overworld():
    def __init__(self, start_level, max_level, surface, create_level):
        
        # setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level
        self.screen_height = screen_height
        self.screen_width = screen_width
        
        # movement logic
        self.moving = False 
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        
        # time 
        self.start_time = pygame.time.get_ticks()
        self.allow_input = False
        self.timer_length = 300
    
    def draw(self, surface):
        self.image = pygame.Surface(((screen_height, screen_width)))
        self.image.fill('red')
    
    def get_input(self):
        # control system for player movement
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_l]:
            self.create_level()
    
    def run(self):
        self.draw(self.display_surface)
        self.get_input()