import pygame

# Initialize pygame
pygame.init()

# Set up the window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Click the box")

# Define colors
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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
top_edge_rect = pygame.Rect(square_x - edge_size, square_y - edge_size, square_size + 2 * edge_size, edge_size)
bottom_edge_rect = pygame.Rect(square_x - edge_size, square_y + square_size, square_size + 2 * edge_size, edge_size)
left_edge_rect = pygame.Rect(square_x - edge_size, square_y - edge_size, edge_size, square_size + 2 * edge_size)
right_edge_rect = pygame.Rect(square_x + square_size, square_y - edge_size, edge_size, square_size + 2 * edge_size)
edge_rects = [top_edge_rect, bottom_edge_rect, left_edge_rect, right_edge_rect]
edge_colors = [edge_color] * 4

# Counters for clicked and connected edges
clicked_edges = 0
connected_edges = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the square is clicked
            if square_rect.collidepoint(event.pos):
                square_on = not square_on
                square_color = YELLOW if square_on else GRAY
            # Check if an edge box is clicked
            for i, edge_rect in enumerate(edge_rects):
                if edge_rect.collidepoint(event.pos):
                    # Change the edge color and update the counters
                    if edge_colors[i] == BLUE:
                        edge_colors[i] = GREEN
                        clicked_edges += 1
                        if clicked_edges == 2:
                            connected_edges += 1
                            clicked_edges = 0
                    else:
                        edge_colors[i] = BLUE
                        if clicked_edges > 0:
                            clicked_edges -= 1

    # Draw the background and the square
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, square_color, square_rect)

    # Draw the edge boxes
    for edge_rect, edge_color in zip(edge_rects, edge_colors):
        pygame.draw.rect(screen, edge_color, edge_rect)

    # Draw the counters
    font = pygame.font.Font(None, 30)
    clicked_edges_text = font.render("Clicked edges: {}".format(clicked_edges), True, RED)
    connected_edges_text = font.render("Connected edges: {}".format(connected_edges), True, RED)
    screen.blit(clicked_edges_text, (10, 10))
    screen.blit(connected_edges_text, (10, 40))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
