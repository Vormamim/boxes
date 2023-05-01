import numpy as np

board = np.zeros((3, 3), dtype=int)

def print_board(board):
    for row in board:
        print('|'.join(['X' if val == 1 else 'O' if val == -1 else ' ' for val in row]))
        print('-' * 5)

def get_input(player):
    while True:
        try:
            col = int(input(f"{player}, choose a column (1-3): ")) - 1
            if col < 0 or col >= 3:
                raise ValueError
            if board[0, col] != 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, try again.")
    return col

def check_win(board):
    for player in [-1, 1]:
        # Check rows
        for row in range(3):
            if all(board[row, col] == player for col in range(3)):
                return player
        # Check columns
        for col in range(3):
            if all(board[row, col] == player for row in range(3)):
                return player
        # Check diagonals
        if all(board[i, i] == player for i in range(3)):
            return player
        if all(board[i, 2-i] == player for i in range(3)):
            return player
    return 0

players = ['Player 1', 'Player 2']
current_player = 0

while True:
    print_board(board)
    col = get_input(players[current_player])
    board[::-1, col][np.where(board[::-1, col] == 0)[0][0]] = (-1 if current_player else 1)
    winner = check_win(board)
    if winner != 0:
        print_board(board)
        print(f"{players[current_player]} wins!")
        break
    if np.count_nonzero(board == 0) == 0:
        print_board(board)
        print("It's a tie!")
        break
    current_player = 1 - current_player
