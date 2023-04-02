import pygame
from Settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obsticale_sprites, SPEED):
        super().__init__(groups)
        self.image = pygame.image.load('Assets\Floors\PNG\Grass.png').convert_alpha() # load player's image
        self.rect = self.image.get_rect(topleft = pos) # set player's position on the screen

        self.direction = pygame.math.Vector2() # create a 2D vector for player's movement direction
        self.speed = SPEED # set player's speed

        self.obsticale_sprites = obsticale_sprites # set obstacles for collision detection

    def input(self):
        keys = pygame.key.get_pressed() # get the keys pressed by the player
        
        # UP / DOWN
        if keys[pygame.K_UP]:
            self.direction.y = -1 # set player's direction upward
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1 # set player's direction downward
        else: self.direction.y = 0 # set player's direction to zero if no UP/DOWN key is pressed

        # LEFT / RIGHT
        if keys[pygame.K_LEFT]:
            self.direction.x = -1 # set player's direction to left
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1 # set player's direction to right
        else: self.direction.x = 0 # set player's direction to zero if no LEFT/RIGHT key is pressed

    def move(self,speed):
        if self.direction.magnitude() != 0: # check if player's direction is not zero
            self.direction = self.direction.normalize() # normalize player's direction

        self.rect.x += self.direction.x * speed # move player horizontally
        self.collision('horizontal') # check for horizontal collisions
        self.rect.y += self.direction.y * speed # move player vertically
        self.collision('vertical') # check for vertical collisions

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obsticale_sprites: # loop through all the obstacles
                if sprite.rect.colliderect(self.rect): # check for collision
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left # adjust player's position to avoid collision
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right # adjust player's position to avoid collision

        if direction == 'vertical':
            for sprite in self.obsticale_sprites: # loop through all the obstacles
                if sprite.rect.colliderect(self.rect): # check for collision
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top # adjust player's position to avoid collision
                    if self.direction.y < 0: # moving up
                        self.rect.top = sprite.rect.bottom # adjust player's position to avoid collision

    def update(self):
        self.input() # get player's input
        self.move(self.speed) # move the player accordingly
