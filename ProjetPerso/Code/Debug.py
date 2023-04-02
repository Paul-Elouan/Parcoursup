# Import the Pygame library and initialize it
import pygame
pygame.init()

# Create a Pygame font object
font = pygame.font.Font(None, 30)

# Define a function that displays debug informations on the Pygame screen
def debug(info, y = 10, x = 10):
    # Get the Pygame display surface
    display_surface = pygame.display.get_surface()
    
    # Render the debug information as text using the font object created earlier, with color white
    debug_surf = font.render(str(info), True, 'White')
    
    # Get the rectangular area that the debug text will occupy on the screen, with its top left corner at the (x, y) position
    debug_rect= debug_surf.get_rect(topleft = (x,y))
    
    # Draw a black rectangle behind the debug text on the Pygame display surface
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    
    # Blit (copy) the rendered debug text onto the Pygame display surface at the position defined by "debug_rect"
    display_surface.blit(debug_surf, debug_rect)
