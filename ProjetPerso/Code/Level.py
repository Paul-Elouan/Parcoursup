# Import required modules and classes
import pygame
from Settings import *
from Tile import Tile
from Player import Player
from Debug import *

# Define a class called Level
class Level:
    # Constructor method for the Level class
    def __init__(self):
        # Get the Pygame display surface
        self.display_surface = pygame.display.get_surface()

        # Create two groups of sprites: visible_sprites and obsticale_sprites
        self.visible_sprites = YSortCameraGroup()
        self.obsticale_sprites = pygame.sprite.Group()

        # Call the "Mapping" method to create tiles and the player
        self.Mapping()

    # Method to create tiles and the player based on a 2D array representing the game world
    def Mapping(self):
        # Iterate over each row and column in the 2D array
        for row_index, row in enumerate(WORLD_MAP): # y
            for column_index, column in enumerate(row): # x
                # Calculate the x and y position of the tile based on its row and column indices
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                # Create a Tile sprite at the calculated position if the value in the 2D array is 'x'
                if column == 'x':
                    Tile((x,y),[self.visible_sprites, self.obsticale_sprites])
                # Create a Player sprite at the calculated position if the value in the 2D array is 'p'
                if column == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obsticale_sprites, SPEED)

    # Method to update and draw the sprites in the "visible_sprites" group
    def run(self):
        # Draw the player sprite and update all the sprites in the "visible_sprites" group
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

# Define a subclass of Pygame's sprite.Group called YSortCameraGroup
class YSortCameraGroup(pygame.sprite.Group):
    # Constructor method for the YSortCameraGroup class
    def __init__(self):
        super().__init__()
        # Get the Pygame display surface and calculate the half width and height of the screen
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_hight = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    # Custom draw method to draw the sprites with respect to the camera
    def custom_draw(self, player):
        # Calculate the camera offset based on the player's position
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_hight

        # Draw each sprite in the group at its offset position
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
