import pygame
from Settings import *
from Tile import Tile
from Player import Player
from Debug import *

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obsticale_sprites = pygame.sprite.Group()
    
        self.Mapping()

    def Mapping(self):
        for row_index, row in enumerate(WORLD_MAP): # y
            for column_index, column in enumerate(row): # x
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'x':
                    Tile((x,y),[self.visible_sprites, self.obsticale_sprites])
                if column == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obsticale_sprites, SPEED)



    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_hight = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_hight

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)