import pygame

# Initialize pygame
pygame.init()

# Set up window
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Circle Grid")

# Set up circle properties
circle_radius = 10
circle_spacing = 100
circle_color = (0, 0, 255)

# Calculate grid dimensions
grid_width = 5 * circle_spacing
grid_height = 5 * circle_spacing

# Calculate grid position to center it
grid_x = (size[0] - grid_width) // 2
grid_y = (size[1] - grid_height) // 2

# Create grid of circles
circles = []
for i in range(5):
    for j in range(5):
        circle_x = grid_x + (i * circle_spacing)
        circle_y = grid_y + (j * circle_spacing)
        circle_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius,
                                  circle_radius * 2, circle_radius * 2)
        circles.append(circle_rect)

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw everything
    screen.fill((255, 255, 255))
    for circle in circles:
        pygame.draw.circle(screen, circle_color, circle.center, circle_radius)
    pygame.display.update()

# Quit pygame properly
pygame.quit()
