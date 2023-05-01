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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up square
square_size = 200
square_x = (size[0] - square_size) // 2
square_y = (size[1] - square_size) // 2
square_rect = pygame.Rect(square_x, square_y, square_size, square_size)
square_on = False
square_color = GRAY

# Set up edge boxes
edge_size = 20
edge_color = BLUE
top_edge_rect = pygame.Rect((square_x-20), square_y - edge_size, (square_size+40), edge_size)
bottom_edge_rect = pygame.Rect(square_x, square_y + square_size, square_size, edge_size)
left_edge_rect = pygame.Rect(square_x - edge_size, square_y, edge_size, square_size)
right_edge_rect = pygame.Rect(square_x + square_size, square_y, edge_size, square_size)
edge_rects = [top_edge_rect, bottom_edge_rect, left_edge_rect, right_edge_rect]
edge_colors = [edge_color] * 4

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
                # Toggle the square on or off
                square_on = not square_on
                square_color = RED if square_on else GRAY
            else:
                # Check if mouse click is on an edge box
                for i, edge_rect in enumerate(edge_rects):
                    if edge_rect.collidepoint(event.pos):
                        # Toggle the edge color on or off
                        if edge_colors[i] == edge_color:
                            edge_colors[i] = YELLOW
                        else:
                            edge_colors[i] = edge_color

    # Draw the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, square_color, square_rect)
    for i, edge_rect in enumerate(edge_rects):
        pygame.draw.rect(screen, edge_colors[i], edge_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
