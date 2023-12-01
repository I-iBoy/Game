import pygame 

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