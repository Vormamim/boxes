import random

grid_size = 4
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
player_score = 0
computer_score = 0

def print_grid():
    for row in grid:
        print('|'.join(row))

def is_valid_move(x, y):
    return 0 <= x < grid_size and 0 <= y < grid_size and grid[x][y] == ' '

def get_available_moves():
    return [(x, y) for x in range(grid_size) for y in range(grid_size) if is_valid_move(x, y)]

def make_move(x, y, player):
    global player_score, computer_score
    grid[x][y] = player
    score = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        while is_valid_move(nx, ny):
            nx += dx
            ny += dy
            score += 1
        if grid[x][y] == 'X':
            player_score += score
        else:
            computer_score += score

print('Welcome to the game!')
print('You are X, and the computer is O.')
print('Your goal is to create the longest connected line of Xs on the board.\n')

while True:
    print_grid()
    print(f"\nPlayer score: {player_score}\nComputer score: {computer_score}\n")
    available_moves = get_available_moves()
    if not available_moves:
        print('No more moves available. Game over!')
        break
    if player_score + computer_score == grid_size**2:
        print('All boxes have been filled. Game over!')
        break
    if player_score > computer_score:
        print('You are winning!')
    elif player_score < computer_score:
        print('The computer is winning!')
    else:
        print('The game is tied.')
    print('\nAvailable moves:')
    for i, move in enumerate(available_moves):
        print(f'{i + 1}. ({move[0] + 1}, {move[1] + 1})')
    choice = int(input('Enter your choice (1-{}): '.format(len(available_moves))))
    x, y = available_moves[choice - 1]
    make_move(x, y, 'X')
    print_grid()
    print('You chose: ({}, {})'.format(x + 1, y + 1))
    computer_move = random.choice(available_moves)
    make_move(*computer_move, 'O')
    print_grid()
    print('Computer chose: ({}, {})'.format(computer_move[0] + 1, computer_move[1] + 1))
