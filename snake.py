import random



board = [[' ']*12 for _ in range(12)]

player1_score = 0
player2_score = 0
game_over = False


# place player 1
row1 = random.randint(0, 11)
col1 = random.randint(0, 11)
board[row1][col1] = 'X'

# place player 2
row2 = random.randint(0, 11)
col2 = random.randint(0, 11)
while row2 == row1 and col2 == col1: # ensure player 2 doesn't overlap with player 1
    row2 = random.randint(0, 11)
    col2 = random.randint(0, 11)
board[row2][col2] = 'O'

# draw the board
for row in board:
    print('+---'*12 + '+')
    print('|' + '|'.join([f' {cell} ' for cell in row]) + '|')
print('+---'*12 + '+')


while not game_over:
    # player 1's turn
    move = input("Player 1's turn. Enter a move (8 for up, 2 for down, 6 for right, 4 for left): ")
    # update player 1's position
    if move == '8' and row1 > 0:
        row1 -= 1
    elif move == '2' and row1 < 11:
        row1 += 1
    elif move == '6' and col1 < 11:
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
    elif move == '2' and row2 < 11:
        row2 += 1
    elif move == '6' and col2 < 11:
        col2 += 1
    elif move == '4' and col2 > 0:
        col2 -= 1
    board[row2][col2] = 'O'
    player2_score += 1

    
    for row in board:
        print('+---'*12 + '+')
        print('|' + '|'.join([f' {cell} ' for cell in row]) + '|')
    print('+---'*12 + '+')

# check for collisions
if row1 == row2 and col1 == col2:
    game_over = True

# determine the winner
if player1_score > player2_score:
    print('Player 1 wins!')
elif player2_score > player1_score:
    print('Player 2 wins!')
else:
    print('The game is tied!')
