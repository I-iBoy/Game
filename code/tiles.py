import pygame 
from support import import_folder
from setting import half_tile_size

class Tile(pygame.sprite.Sprite):
	def __init__(self,x, y, size):
		super().__init__()
		
		# tile setup
		self.image = pygame.Surface((size,size))
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = (x, y))
	
	def update(self,x_shift):
		# move the tile 
		self.rect.x += x_shift

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

class AnimatedTile(Tile):
    def __init__(self, size, x, y, path=None, value = 0):
        super().__init__(size, x, y)
        # self.frames = import_folder(path)
        # self.frame_index = 0
        # self.image = self.frames[self.frame_index]
        # self.value = value
    
    # def animate(self):
    #     self.frame_index += self.animation_speed
    #     if self.frame_index >= len(self.frames):
    #         self.frame_index = 0
        
        # self.image = self.frames[int(self.frame_index)]
    
    def update(self, x_shift):
        # self.animate()											#NOTE - if the coin has multiple images / frames -> for the animation 
        self.rect.x += x_shift

class Coin(StaticTile):
    def __init__(self, x, y, size, value):
        super().__init__(size, x, y, pygame.image.load('G:\Programmieren\Projekte\Game\images\coins\silver.png').convert_alpha())
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.rect = self.image.get_rect(center = (center_x, center_y))
        self.value = value