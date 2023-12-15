import pygame 
from support import import_folder

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		
		# tile setup
		self.image = pygame.Surface((size,size))
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = pos)
	
	def update(self,x_shift):
		# move the tile 
		self.rect.x += x_shift

class AnimatedTile(Tile):
    def __init__(self, size, x, y, path, value = 0):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.value = value
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]
    
    def update(self, x_shift):
        # self.animate()											#NOTE - if the coin has multiple images / frames -> for the animation 
        self.rect.x += x_shift

class Coin(AnimatedTile):
    def __init__(self, size, x, y, path, value):
        super().__init__(size, x, y, path)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.rect = self.image.get_rect(center = (center_x, center_y))
        self.value = value