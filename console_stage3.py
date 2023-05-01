import random

# create a 4x4 grid
grid = [['-' for _ in range(4)] for _ in range(4)]

# function to check if a player has won
def check_win(player):
    # check rows
    for row in grid:
        if row == [player] * 4:
            return True
    # check columns
    for j in range(4):
        if all(grid[i][j] == player for i in range(4)):
            return True
    # check diagonals
    if all(grid[i][i] == player for i in range(4)) or all(grid[i][3-i] == player for i in range(4)):
        return True
    return False

# function to print the grid
def print_grid():
    for row in grid:
        print(' '.join(row))
    print()

# function to make the computer move
def computer_move(player):
    # first, check if the computer can win
    for i in range(4):
        for j in range(4):
            if grid[i][j] == '-':
                grid[i][j] = player
                if check_win(player):
                    return (i, j)
                grid[i][j] = '-'
    # next, check if the player can win and block them
    for i in range(4):
        for j in range(4):
            if grid[i][j] == '-':
                grid[i][j] = 'X' if player == 'O' else 'O'
                if check_win('X' if player == 'O' else 'O'):
                    grid[i][j] = player
                    return (i, j)
                grid[i][j] = '-'
    # otherwise, make a random move
    while True:
        i, j = random.randint(0, 3), random.randint(0, 3)
        if grid[i][j] == '-':
            grid[i][j] = player
            return (i, j)

# main game loop
scores = {'X': 0, 'O': 0}
player_turn = True
while '-' in [cell for row in grid for cell in row]:
    print_grid()
    if player_turn:
        row = int(input("Enter row number (1-4): ")) - 1
        col = int(input("Enter column number (1-4): ")) - 1
        if grid[row][col] != '-':
            print("Invalid move, try again.")
            continue
        grid[row][col] = 'X'
    else:
        row, col = computer_move('O')
        print("Computer selects row", row + 1, "column", col + 1)
    # check for a win
    if check_win('X'):
        print_grid()
        print("Player wins!")
        scores['X'] += 1
        break
    if check_win('O'):
        print_grid()
        print("Computer wins!")
        scores['O'] += 1
        break
    # switch turns
    player_turn = not player_turn

# print the final score
print("Final score:")
print("Player:", scores['X'])
print("Computer:", scores['O'])
