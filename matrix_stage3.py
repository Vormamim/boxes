import pygame

# Initialize pygame
pygame.init()

# Set up window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Circle Line")


# Set up colors
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
click_sound = pygame.mixer.Sound("clicked_sound.mp3")

# Set up circles
circle_radius = 10
circle_distance = 100
circle_x1 = (size[0] // 2) - (circle_distance // 2) - circle_radius
circle_x2 = (size[0] // 2) + (circle_distance // 2) - circle_radius
circle_y = size[1] // 2
circle_color1 = RED
circle_color2 = RED
circle1_active = False
circle2_active = False

# Set up line
line_thickness = 5
line_color = GREEN
line_rect = pygame.Rect(0, 0, 0, line_thickness)
line_active = False

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Toggle circle 1 on/off
            if not circle1_active and abs(mouse_pos[0] - (circle_x1 + circle_radius)) <= circle_radius and abs(mouse_pos[1] - (circle_y + circle_radius)) <= circle_radius:
                circle1_active = True
                circle_color1 = GREEN
            # Toggle circle 2 on/off and draw line if both circles are active
            elif not circle2_active and abs(mouse_pos[0] - (circle_x2 + circle_radius)) <= circle_radius and abs(mouse_pos[1] - (circle_y + circle_radius)) <= circle_radius:
                circle2_active = True
                circle_color2 = GREEN
                if circle1_active:
                    line_rect = pygame.Rect(circle_x1 + circle_radius, circle_y + (line_thickness // 2), circle_distance, line_thickness)
                    line_active = True
                    click_sound.play()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, circle_color1, (circle_x1 + circle_radius, circle_y + circle_radius), circle_radius)
    pygame.draw.circle(screen, circle_color2, (circle_x2 + circle_radius, circle_y + circle_radius), circle_radius)
    if line_active:
        pygame.draw.rect(screen, line_color, line_rect)
    pygame.display.update()

# Quit pygame properly
pygame.quit()
