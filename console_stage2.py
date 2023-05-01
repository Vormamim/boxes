import random

# initialize the game board and scores
game_board = [['-' for _ in range(4)] for _ in range(4)]
player_score = 0
computer_score = 0

# function to print the game board and scores
def print_board():
    print('  1 2 3 4')
    for i in range(4):
        print(f"{i+1} {' '.join(game_board[i])}")
    print(f"\nScore: P1 - {player_score}  Computer - {computer_score}\n")

# function to check if a given cell is valid
def is_valid_cell(row, col):
    if row < 0 or row > 3 or col < 0 or col > 3:
        return False
    if game_board[row][col] != '-':
        return False
    return True

# function to check if the game is over
def is_game_over():
    for i in range(4):
        for j in range(4):
            if game_board[i][j] == '-':
                return False
    return True

# main game loop
print("Welcome to the game!")
print("You are X, the computer is O.")
print("Choose a cell by entering row and column numbers (e.g. 1 2).")

while not is_game_over():
    # player's turn
    print_board()
    valid_input = False
    while not valid_input:
        row, col = map(int, input("P1's turn: ").split())
        row -= 1  # adjust for 0-based indexing
        col -= 1
        if is_valid_cell(row, col):
            game_board[row][col] = 'X'
            player_score += 1
            valid_input = True
        else:
            print("Invalid input. Please choose an empty cell.")

    # computer's turn
    valid_input = False
    while not valid_input:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if is_valid_cell(row, col):
            game_board[row][col] = 'O'
            computer_score += 1
            valid_input = True

# print final scores
print_board()
if player_score > computer_score:
    print("Congratulations, you win!")
elif player_score < computer_score:
    print("Sorry, the computer wins.")
else:
    print("It's a tie!")
