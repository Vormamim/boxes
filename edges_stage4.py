import pygame

# Initialize pygame
pygame.init()

# Set up colors
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Set up window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Edge Count")

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
bottom_edge_rect = pygame.Rect((square_x-20), square_y + square_size, (square_size+40), edge_size)
left_edge_rect = pygame.Rect(square_x - edge_size, square_y, edge_size, square_size)
right_edge_rect = pygame.Rect(square_x + square_size, square_y, edge_size, square_size)
edge_rects = [top_edge_rect, bottom_edge_rect, left_edge_rect, right_edge_rect]
edge_colors = [edge_color] * 4
connected_edges = 0

# Set up font
font = pygame.font.SysFont('Calibri', 25, True, False)

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Toggle square on/off
            if square_rect.collidepoint(mouse_pos):
                square_on = not square_on
                if square_on:
                    square_color = GREEN
                else:
                    square_color = GRAY
                    connected_edges = 0
                    for i in range(len(edge_colors)):
                        if edge_colors[i] == YELLOW:
                            connected_edges -= 1
                            edge_colors[i] = edge_color
            # Toggle edge on/off and count connected edges
            for i in range(len(edge_rects)):
                if edge_rects[i].collidepoint(mouse_pos):
                    if square_on:
                        if edge_colors[i] == BLUE:
                            edge_colors[i] = YELLOW
                            connected_edges += 1
                        elif edge_colors[i] == YELLOW:
                            edge_colors[i] = BLUE
                            connected_edges -= 1

    # Draw everything
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, square_color, square_rect)
    for i in range(len(edge_rects)):
        pygame.draw.rect(screen, edge_colors[i], edge_rects[i])
    text = font.render("Connected Edges: " + str(connected_edges), True, (0, 0, 0))
    screen.blit(text, (5, 5))
    pygame.display.update()

# Quit pygame properly
pygame.quit()
