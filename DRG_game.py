import random

# Define the game function
def play_game():
    # Set up the game board
    board = [[0] * 10 for i in range(10)]
    player_row, player_col = 5, 5
    computer_row, computer_col = 2, 2
    player_length, computer_length = 1, 1

    # Draw the initial board
    def draw_board():
        print("+---" * 10 + "+")
        for row in range(10):
            print("| ", end="")
            for col in range(10):
                if row == player_row and col == player_col:
                    print("X ", end="")
                elif row == computer_row and col == computer_col:
                    print("O ", end="")
                elif board[row][col]:
                    print("X ", end="")
                else:
                    print("  ", end="")
                print("| ", end="")
            print()
            print("+---" * 10 + "+")

    # Main game loop
    while True:
        # Draw the board
        draw_board()

        # Check for collisions
        if board[player_row][player_col]:
            print("You lost!")
            break
        if board[computer_row][computer_col]:
            print("You won!")
            break

        # Player turn
        print("Your turn!")
        direction = input("Which direction do you want to go? (up, down, left, right): ")
        if direction == "up":
            player_row -= 1
        elif direction == "down":
            player_row += 1
        elif direction == "left":
            player_col -= 1
        elif direction == "right":
            player_col += 1
        else:
            print("Invalid direction.")

        # Computer turn
        print("Computer's turn!")
        possible_moves = []
        if computer_row > 0 and not board[computer_row - 1][computer_col]:
            possible_moves.append((-1, 0))
        if computer_row < 9 and not board[computer_row + 1][computer_col]:
            possible_moves.append((1, 0))
        if computer_col > 0 and not board[computer_row][computer_col - 1]:
            possible_moves.append((0, -1))
        if computer_col < 9 and not board[computer_row][computer_col + 1]:
            possible_moves.append((0, 1))

        if possible_moves:
            move = random.choice(possible_moves)
            computer_row += move[0]
            computer_col += move[1]
        else:
            print("Computer has no moves!")

        # Update the board
        board[player_row][player_col] = 1
        for i in range(player_length):
            if player_row - i >= 0:
                board[player_row - i][player_col] = 1
        for i in range(computer_length):
            if computer_row - i >= 0:
                board[computer_row - i][computer_col] = 1

        # Update the lengths
        player_length += 1
        computer_length += 1

play_game()
