import pygame, sys
from Settings import *
from Level import *
from Debug import debug

class Game:
    def __init__(self):
        pygame.init()  # initialize Pygame module
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))  # set window size
        pygame.display.set_caption('Lands of the Forgotten Souls')  # set window title
        #icon_32x32 = pygame.image.load('').convert_alpha()  # load window icon 
        #pygame.display.set_icon(icon_32x32)  # set window icon 
        self.clock = pygame.time.Clock()  # create Pygame clock object to manage FPS

        self.level = Level()  # create Level object

    def run(self):
        while True:  # main game loop
            for event in pygame.event.get():  # loop through Pygame events
                if event.type == pygame.QUIT:  # if the user clicks the close button
                    pygame.quit()  # quit Pygame module
                    sys.exit()  # exit program

            self.screen.fill('Black')  # fill screen with black color
            self.level.run()  # run the game level
            pygame.display.update()  # update the screen
            self.clock.tick(FPS)  # limit FPS to the desired value

if __name__ == '__main__':
    game = Game()  # create Game object
    game.run()  # run the game
