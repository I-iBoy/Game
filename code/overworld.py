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
        
        # background
        self.opacity = 80
    
    def background(self):
        # background image
        bg = pygame.image.load('./images/overworld/christmas_bg.jpg')
        scaled_bg = pygame.transform.scale(bg, (screen_width, screen_height))
        self.display_surface.blit(scaled_bg, (0, 0))
        
        # background overlay 
        self.image = pygame.Surface((screen_height, screen_width))
        self.image.fill('black')
        scaled_overlay = pygame.transform.scale(self.image, (screen_width, screen_height))
        transparent_overlay = scaled_overlay.set_alpha(self.opacity)
        self.display_surface.blit(scaled_overlay, (0, 0))
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_l]:
            self.create_level(self.current_level)
    
    def run(self):
        self.background()
        self.get_input()