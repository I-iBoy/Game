import pygame
from tiles import Tile, Coin 
from player import Player
from setting import tile_size, screen_width, font_1
from support import import_csv_layout

class Level():
    
    def __init__(self, surface, create_overworld, change_health, level_data):
        
        # level setup
        self.display_surface = surface 
        self.setup_level(level_data)
        self.world_shift = 0
        self.player_speed = 2.5
        # This may only be changed if the Player Speed has been changed (always must be the same)
        
        self.world_shift_setup = self.player_speed * 10
        self.current_x = 0
        
        # setup for extras 
        self.coins_amount = 0 
        
        # player setup
        self.player_on_ground = False
        
        
        # Tile spawn setup 
        # coins
        # coin_layout = import_csv_layout(level_data['coins'])
        # self.coin_sprites = self.create_tile_group(level_data, 'coins')
    
    def setup_level(self, layout):
        # create all sprites 
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coins = pygame.sprite.Group()
        self.sprite_group = pygame.sprite.Group()
        
        # check every row and every colum
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
				
                # if there is a X => place a block
                if cell == 'X':
                    tile = Tile(x, y,tile_size)
                    self.tiles.add(tile)
                
                # if there is a P => place the player
                elif cell == 'P':
                    player = Player((x,y),tile_size)
                    self.player.add(player)
                
                # if there is a C => place a coin
                elif cell == 'C':
                    coin = Coin(x, y, tile_size)
                    self.coins.add(coin)
    
    # def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell != ' ':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    
                    # if type == 'coins':
                    if cell == 'C':
                        sprite = Coin(x, y, tile_size) # ... => File path to the coin image 
                        sprite_group.add(sprite)
        
        return sprite_group
    
    def scroll_x(self):
        # scroll setup
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        # left site 
        if player_x < (screen_width / 3) and direction_x < 0:
            self.world_shift = self.world_shift_setup
            player.speed = 0
        
        # right site
        elif player_x > screen_width - (screen_width / 3) and direction_x > 0:
            self.world_shift = self.world_shift_setup * -1
            player.speed = 0
        
        # no scroll
        else:
            self.world_shift = 0
            player.speed = player.speed_setup
    
    def horizontal_movement_collision(self):
        # setup for horizontal movement
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        # check if a block left or right besides the player
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                
                # left
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.current_x = player.rect.left
                
                # right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.current_x = player.rect.right
    
    def vertical_movement_collision(self):
        # setup for horizontal movement
        player = self.player.sprite
        player.get_gravity()
        
        # process player on ground
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                
                # player is on ground 
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                
                # player is not on ground
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        
        #!SECTION
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
    
    def check_player_on_ground(self):
        
        # check for player on ground
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False
    
    def check_coin_collisions(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite, self.coins, True)
        if collided_coins:
            for coin in collided_coins:
                # self.change_coins(coin.value)
                self.coins_amount += 1
                print("coin collision")
    
    def coin_text(self):
        pygame.font.init()
        
        x = tile_size * 1
        y = tile_size * 0.37
        
        my_font = pygame.font.Font((font_1), 25)
        text_surface = my_font.render(str(self.coins), True, (255,255,255))
        
        self.display_surface.blit(text_surface, (x, y))
    
    def update_and_draw(self):
        # level Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        # player
        self.player.update()
        self.player.draw(self.display_surface)
        
        # coins
        self.coins.draw(self.display_surface)
    
    def run(self):
        self.update_and_draw()
        self.scroll_x()
        
        # player
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.check_player_on_ground()
        self.player.draw(self.display_surface)