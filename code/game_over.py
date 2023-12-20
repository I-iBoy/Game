import pygame 
from setting import screen_height, screen_width
from setting import font_1

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
        
        if keys[pygame.K_BACKSPACE]:
            self.create_overworld()
        elif keys[pygame.K_SPACE]:
            self.create_level()
    
    def set_game_hight_score(self):
        file = open('./game_data/high_score.txt', 'r')
        old_hight_score = file.read()
        
        if int(old_hight_score) < int(self.score):
            file1 = open('./game_data/high_score.txt', 'w')
            file1.write(str(self.score))
            file1.close()
        else:
            self.score = old_hight_score
        
        file.close()
    
    def reset_hight_score(self):
        file = open('./test/high_score.txt', 'w')
        file.write(str(0))
        file.close()
    
    def text(self, text, x, y, font_type=None):
        pygame.font.init()
        
        # font size 
        if font_type == 'big':
            font_size = 55
        elif font_type == 'small':
            font_size = 35
        elif font_type == None:
            font_size = 25
        
        
        
        my_font = pygame.font.Font((font_1), font_size)
        text_surface = my_font.render(text, True, (255,255,255))
        
        self.display_surface.blit(text_surface, (x, y))
    
    def run(self):
        self.death_screen()
        self.get_input()
        
        self.set_game_hight_score()
        
        # draw every font 
        self.text('GAME OVER', 480, 150, 'big')
        self.text((f'High Score:    {self.score}'), 480, 250, 'small')
        self.text('Press BACKSPACE to switch to the Home Screen', 480, 350)
        self.text('Press SPACE to play again', 480, 400)