import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boxes Demonstration")

# Set up colors
BLUE = (153, 204, 255)
DK_BLUE=(51, 102, 255)
RED=(255,0,0)
YELLOW = (255, 255, 0)

# Draw the background
screen.fill(BLUE)

# Update the display
pygame.display.flip()

# set up the grid
cell_size = 80
x_offset = (screen_width - (cell_size * 5)) // 2
y_offset = (screen_height - (cell_size * 5)) // 2
for row in range(5):
    for col in range(5):
        rect = pygame.Rect(x_offset + col * cell_size, y_offset + row * cell_size, cell_size, cell_size)
        top_left = rect.topleft
        # center=rect.center
        pygame.draw.rect(screen, DK_BLUE, rect, 1)
        # pygame.draw.rect(screen, RED, pygame.Rect(top_left[0]-3, top_left[1]-3, 6, 6))
        pygame.draw.rect(screen, RED, pygame.Rect(top_left[0], top_left[1], 6, 6))
        bottom_right = rect.bottomright
        pygame.draw.rect(screen, YELLOW, pygame.Rect(bottom_right[0]-6, bottom_right[1]-6, 6, 6))



# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()
    

# Quit Pygame
pygame.quit()
