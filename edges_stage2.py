import pygame

# Initialize pygame
pygame.init()

# Set up window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clickable Square")

# Set up colors
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

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
edge_rects = [
    pygame.Rect(square_x - edge_size, square_y - edge_size, square_size + 2*edge_size, edge_size),
    pygame.Rect(square_x - edge_size, square_y + square_size, square_size + 2*edge_size, edge_size),
    pygame.Rect(square_x - edge_size, square_y, edge_size, square_size),
    pygame.Rect(square_x + square_size, square_y, edge_size, square_size)
]
edge_colors = [edge_color] * 4

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if square is clicked
            if square_rect.collidepoint(event.pos):
                square_on = not square_on
                square_color = YELLOW if square_on else GRAY
            # Check if an edge box is clicked
            for i, edge_rect in enumerate(edge_rects):
                if edge_rect.collidepoint(event.pos):
                    if edge_colors[i] == BLUE:
                        edge_colors[i] = YELLOW
                    else:
                        edge_colors[i] = BLUE

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw square and edges
    pygame.draw.rect(screen, square_color, square_rect)
    for edge_rect, edge_color in zip(edge_rects, edge_colors):
        pygame.draw.rect(screen, edge_color, edge_rect)

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
