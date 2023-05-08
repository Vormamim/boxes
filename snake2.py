import random
board_size=5

# set up the game board
board = [[' ']*board_size for _ in range(board_size)]
player1_positions = []
player2_positions = []

# place player 1
row1 = random.randint(0, board_size-1)
col1 = random.randint(0, board_size-1)
board[row1][col1] = 'X'

# place player 2
row2 = random.randint(0, board_size-1)
col2 = random.randint(0, board_size-1)
while row2 == row1 and col2 == col1: # ensure player 2 doesn't overlap with player 1
    row2 = random.randint(0, board_size-1)
    col2 = random.randint(0, board_size-1)
board[row2][col2] = 'O'

# draw the board
for row in board:
    print('+---'*board_size + '+')
    print('|' + '|'.join([f' {cell} ' for cell in row]) + '|')
print('+---'*board_size + '+')

# start the game loop
player1_score = 0
player2_score = 0
game_over = False

while not game_over:
    # player 1's turn
    move = input("Player 1's turn. Enter a move (8 for up, 2 for down, 6 for right, 4 for left): ")
    # update player 1's position
    if move == '8' and row1 > 0:
        row1 -= 1
    elif move == '2' and row1 < board_size-1:
        row1 += 1
    elif move == '6' and col1 < board_size-1:
        col1 += 1
    elif move == '4' and col1 > 0:
        col1 -= 1
    board[row1][col1] = 'X'
    player1_score += 1

    # player 2's turn
    move = input("Player 2's turn. Enter a move (8 for up, 2 for down, 6 for right, 4 for left): ")
    # update player 2's position
    if move == '8' and row2 > 0:
        row2 -= 1
    elif move == '2' and row2 < board_size-1:
        row2 += 1
    elif move == '6' and col2 < board_size-1:
        col2 += 1
    elif move == '4' and col2 > 0:
        col2 -= 1
    board[row2][col2] = 'O'
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
    for row in board:
        print('+---'*board_size + '+')
        print('|' + '|'.join([f' {cell} ' for cell in row]) + '|')
    print('+---'*board_size + '+')


# determine the winner
if player1_score > player2_score:
    print('Player 1 wins!')
elif player2_score > player1_score:
    print('Player 2 wins!')
else:
    print('The game is tied!')
