import pygame 
from setting import screen_height, screen_width

class GameOver():
    def __init__(self, surface, create_level, create_overworld, score):
        
        self.create_level = create_level
        self.create_overworld = create_overworld
        self.score = score
        self.display_surface = surface
        
        # background
        self.opacity = 80
    
    def death_screen(self):
        # background image
        bg = pygame.image.load('./images/overworld/christmas_bg.jpg')
        scaled_bg = pygame.transform.scale(bg, (screen_width, screen_height))
        self.display_surface.blit(scaled_bg, (0, 0))
        
        # background overlay 
        self.image = pygame.Surface((screen_height, screen_width))
        self.image.fill('black')
        scaled_overlay = pygame.transform.scale(self.image, (screen_width, screen_height))
        scaled_overlay.set_alpha(self.opacity)
        self.display_surface.blit(scaled_overlay, (0, 0))
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_KP_ENTER]:
            self.create_level()
    
    def set_game_hight_score(self):
        file = open('./game_data/hight_score.txt', 'r')
        old_hight_score = file.read()
        
        if int(old_hight_score) < int(self.score):
            file1 = open('./game_data/hight_score.txt', 'w')
            file1.write(str(self.score))
            file1.close()
        
        file.close()
    
    def reset_hight_score(self):
        file = open('./test/hight_score.txt', 'w')
        file.write(str(0))
        file.close()
    
    def run(self):
        self.death_screen()
        self.get_input()
        
        self.set_game_hight_score()