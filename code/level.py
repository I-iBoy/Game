import pygame
from tiles import Tile
from player import Player
from setting import tile_size


class Level():
    
    def __init__(self, level_data, surface):
        # level_data is our tile map layout
        
        # level setup
        self.display_surface = surface 
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
    
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
				
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player = Player((x,y),tile_size)
                    self.player.add(player)
    
    def sroll_x(self):
        pass
    
    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        self.player.update()
        self.player.draw(self.display_surface)