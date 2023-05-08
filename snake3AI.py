import random
import os

def cs():
    os.system("cls" if os.name == "nt" else "clear")
    


board_size = 5
cs()

# set up the game board
board = [[' ']*board_size for _ in range(board_size)]
obstacle_positions = [(2, 2), (3, 3), (4, 4)]


# place player 1
row1 = random.randint(0, board_size-1)
col1 = random.randint(0, board_size-1)
board[row1][col1] = 'X'
player1_positions = [(row1, col1)]

# place player 2
row2 = random.randint(0, board_size-1)
col2 = random.randint(0, board_size-1)
while row2 == row1 and col2 == col1:
    row2 = random.randint(0, board_size-1)
    col2 = random.randint(0, board_size-1)
board[row2][col2] = 'O'
player2_positions = [(row2, col2)]

def draw_board(board_size, player1_positions, player2_positions):
    board = ""
    for row in range(board_size):
        for col in range(board_size):
            if (row, col) in player1_positions:
                board += " X "
            elif (row, col) in player2_positions:
                board += " O "
            else:
                board += " - "
        board += "\n"
    print(board)


draw_board(board_size, player1_positions, player2_positions)


# start the game loop
player1_score = 0
player2_score = 0
game_over = False

while not game_over:
    # player 1's turn
    move = input("Player 1's turn. Enter a move (8 for up, 2 for down, 6 for right, 4 for left): ")
    # update player 1's position
    new_row1 = row1
    new_col1 = col1
    # check to see if the move is valid
    
    if 
    
    if move == '8' and row1 > 0:
        new_row1 -= 1
    elif move == '2' and row1 < board_size-1:
        new_row1 += 1
    elif move == '6' and col1 < board_size-1:
        new_col1 += 1
    elif move == '4' and col1 > 0:
        new_col1 -= 1
    if (new_row1, new_col1) in player1_positions or (new_row1, new_col1) in player2_positions: # check for collision
        print("Collision! Player 1 crashed into Player 2.")
        game_over = True
    else:
        board[row1][col1] = ' '
        board[new_row1][new_col1] = 'X'
        player1_positions.append((new_row1, new_col1))
        row1 = new_row1
        col1 = new_col1
        player1_score += 1

    # player 2's turn (computer)
    if player2_score > player1_score: # if the computer is winning, try to end the game
        if row2 > 0 and (row2-1, col2) not in player1_positions and (row2-1, col2) not in player2_positions: # move up
            row2 -= 1
        elif row2 < board_size-1 and (row2+1, col2) not in player1_positions and (row2+1, col2) not in player2_positions: # move down
            row2 += 1
        elif col2 > 0 and (row2, col2-1) not in player1_positions and (row2, col2-1) not in player2_positions: # move left
            col2 -= 1
        elif col2 < board_size-1 and (row2, col2+1) not in player1_positions and (row2, col2+1) not in player2_positions: # move right
            col2 += 1
        else:
            # if the computer cannot move, end the game
            game_over = True
            print("Game over! Player 2 wins!")
    else:
        # if the computer is not winning, try to score a point
        if col2 < board_size-1 and (row2, col2+1) not in player1_positions and (row2, col2+1) not in player2_positions: # move right
            col2 += 1
        elif row2 < board_size-1 and (row2+1, col2) not in player1_positions and (row2+1, col2) not in player2_positions: # move down
            row2 += 1
        elif col2 > 0 and (row2, col2-1) not in player1_positions and (row2, col2-1) not in player2_positions: # move left
            col2 -= 1
        elif row2 > 0 and (row2-1, col2) not in player1_positions and (row2-1, col2) not in player2_positions: # move up
            row2 -= 1
        else:
            # if the computer cannot move, end the game
            game_over = True
            print("Game over! Player 1 wins!")
        #update player 2's position
        board[row2][col2] = 'O'
        player2_positions.append((row2, col2))
        player2_score += 1
            

        # check for collisions

        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == 'X':
                    player1_positions.append((i, j))
                elif board[i][j] == 'O':
                    player2_positions.append((i, j))
            if set(player1_positions) & set(player2_positions):
                game_over = True
            
        # draw the board
        cs()
        draw_board(board_size, player1_positions, player2_positions)
        print(player1_score, player2_score)
    
# determine the winner
if player1_score > player2_score:
    print('Player 1 wins!')
elif player2_score > player1_score:
    print('Player 2 wins!')
else:
    print('The game is tied!')

    
