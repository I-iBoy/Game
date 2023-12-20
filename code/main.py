import pygame, sys
from setting import screen_width, screen_height, level_map
from overworld import Overworld
from level import Level
from game_over import GameOver

class Game():
    def __init__(self):
        
        # game attributes
        self.max_level = 0
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0
        self.level_map = level_map
        
        # overworld creation
        self.overworld = Overworld(display_surface, self.create_level)
        self.status = 'overworld'
        
        # self.game_over = GameOver(display_surface, self.create_level, self.create_overworld, 0)
        # self.status = 'game_over'
    
    def create_level(self):
        self.level = Level(display_surface, self.create_overworld,  self.create_game_over ,self.level_map)
        self.status = 'level'
    
    def create_overworld(self):
        self.overworld = Overworld(display_surface, self.create_level)
        self.status = 'overworld'
    
    def create_game_over(self, score):
        self.game_over = GameOver(display_surface, self.create_level, self.create_overworld, score)
        self.status = 'game_over'
    
    def change_coins(self, amount):
        self.coins += amount
    
    def change_health(self, amount):
        self.cur_health += amount
    
    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(display_surface, self.create_level)
            self.status = 'overworld'
    
    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'game_over':
            self.game_over.run()
        else:
            self.level.run()
            self.check_game_over()

# Pygame setup
pygame.init()
display_surface = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

# window setup
pygame.display.set_caption('Winter Game')
pygame_icon = pygame.image.load('./images/window/tree.png')
pygame.display.set_icon(pygame_icon)

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            pygame.quit()
            sys.exit()
    
    display_surface.fill('black')
    game.run()
    
    pygame.display.update()
    clock.tick(60)