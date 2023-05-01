import pygame
'''
In this version of the code, we create a list of dictionaries called circles, where each dictionary represents a circle and contains two keys: rect (a pygame.Rect object representing the circle's position and size) and color (a tuple representing the circle's color).

In the main game loop, we check for mouse button clicks using pygame.MOUSEBUTTONDOWN. If a click occurs, we loop through the circles list and check if the mouse position collides with each circle's rect using pygame.Rect.collidepoint(). If a collision occurs, we toggle the circle's color between GRAY and RED.

Finally, we draw the circles using pygame.draw.ellipse() and update the display using pygame.display.update().
'''

# Initialise pygame
pygame.init()

# Set up colours
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up window
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Circle Grid")
click_sound = pygame.mixer.Sound("clicked_sound.mp3")

# Set up grid
grid_size = 5
circle_size = 20
circle_spacing = 100
grid_offset = ((size[0] - ((grid_size - 1) * circle_spacing + grid_size * circle_size)) // 2,
               (size[1] - ((grid_size - 1) * circle_spacing + grid_size * circle_size)) // 2)
circles = []
for row in range(grid_size):
    for col in range(grid_size):
        circle_rect = pygame.Rect(col * (circle_size + circle_spacing) + grid_offset[0],
                                  row * (circle_size + circle_spacing) + grid_offset[1],
                                  circle_size, circle_size)
        circles.append({'rect': circle_rect, 'color': GRAY})

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
            for circle in circles:
                if circle['rect'].collidepoint(mouse_pos):
                    if circle['color'] == GRAY:
                        circle['color'] = RED
                        click_sound.play()
                        
                    else:
                        circle['color'] = GRAY
                        click_sound.stop()

    # Draw everything
    screen.fill((255, 255, 255))
    for circle in circles:
        pygame.draw.ellipse(screen, circle['color'], circle['rect'])
    pygame.display.update()

# Quit pygame properly
pygame.quit()
