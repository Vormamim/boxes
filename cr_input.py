import pygame
from pygame.locals import *
import sys

# Initialize pygame
pygame.init()

# Create a window 300 x 300
screen = pygame.display.set_mode((300, 300))
# Set the title of the window
pygame.display.set_caption("Demo: Keyboard Input")
# Init the game clock
clock = pygame.time.Clock()

# Create an empty text string
text = ""

#create an empty list to store text inputs
text_list = []

# Create a font object to display text
font = pygame.font.Font(None, 24)

# Create a box to allow text input
box = pygame.Rect(10, 10, 280, 30)  # x, y, width, height

# Main game loop
while True:
    # Get the events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Get keyboard input
        elif event.type == pygame.KEYDOWN:
            # If keydown is enter, break the loop
            if event.key == pygame.K_RETURN:
                #add text to list
                text_list.append(text)
                print(text_list)
                break
            # If keydown is backspace, delete the last character
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            # Else add the character to the text
            else:
                text += event.unicode

    # Update text input object
    text_surface = font.render(text, True, (0, 0, 0))
    

    

    # Draw the screen
    screen.fill((255, 255, 255))
    # Draw the text input onto the screen
    screen.blit(text_surface, (10, 10))
    # Draw the box onto the screen
    pygame.draw.rect(screen, (0, 0, 0), box, 2)

    # Update the display
    pygame.display.update()


