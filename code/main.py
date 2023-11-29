import pygame
from setting import *
from level import Level

class Main():
    
    def __init__(self):
        # display setup
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Winter Game")
        self.clock = pygame.time.Clock()    
        self.level = Level(level_map, self.screen)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                # quit the game by pressing the cross button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                # quit the game by pressing ESCAPE
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            
            self.level.run()
            
            # update 60 times per second
            pygame.display.update()
            self.clock.tick(60)



if __name__ == "__main__":
    main = Main()
    main.run()