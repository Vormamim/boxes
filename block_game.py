import pygame
from pygame.locals import *
import sys
import random

# Initialize pygame
pygame.init()

# Create a window 300 x 600
screen = pygame.display.set_mode((300, 600))

#set the title of the window
pygame.display.set_caption("Demo:Some Game")

#set the game clock
clock = pygame.time.Clock()

#create player 1 as a red rectangle 30x30 which starts at 0,0
player1 = pygame.Rect(0, 0, 30, 30)

#set player 1 sound
player1_sound = pygame.mixer.Sound("clicked_sound.mp3")

#set player 2 sound
player2_sound = pygame.mixer.Sound("start_sound.mp3")

#create player 2 as a blue rectangle 30x30 which starts at 270,570
player2 = pygame.Rect(270, 570, 30, 30)

#set total player 1 moves to 0
player1_moves = 0

#create a list of the player 1 moves as x,y coordinates
player1_move_list = []

#create a list of the player 2 moves as x,y coordinates
player2_move_list = []

while True:
    # Draw the game board
    screen.fill((0, 0, 0))
    
    # draw a black rectangle for the game area
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, 600), 5)
    #create a grid of 10 x 20
    grid = []

    for row in range(20):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(10):
            grid[row].append(0)  # Append a cell
            #draw a light grey rectangle for each cell
            pygame.draw.rect(screen, (200, 200, 200), (column*30, row*30, 30, 30), 1)
            
    #draw the player rectangles
    pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 255), player2)
    
    clock.tick(30)  # Add the frame rate to the main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if check_move(player1, player1.x, player1.y - 30):
            player1.y -= 30
            player1_moves += 1
            player1_move_list.append((player1.x, player1.y))
            player1_sound.play()
            grid[player1.y//30][player1.x//30] = "P1"  # Update the grid with player 1's move
    if keys[pygame.K_s]:
        if check_move(player1, player1.x, player1.y + 30):
            player1.y += 30
            player1_moves += 1
            player1_move_list.append((player1.x, player1.y))
            player1_sound.play()
            grid[player1.y//30][player1.x//30] = "P1"
    if keys[pygame.K_a]:
        if check_move(player1, player1.x - 30, player1
