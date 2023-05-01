import pygame

# Initialize Pygame
pygame.init()

# Set up the window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Square Clicker")

# Set up colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Set up square
square_size = 200
square_x = (size[0] - square_size) // 2
square_y = (size[1] - square_size) // 2
square_rect = pygame.Rect(square_x, square_y, square_size, square_size)
square_color = GRAY

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse click is inside the square
            if square_rect.collidepoint(event.pos):
                # Change the color of the square
                square_color = RED

    # Draw the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, square_color, square_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
