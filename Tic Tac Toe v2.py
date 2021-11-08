def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Select X or O ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# player_input()

def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board, mark):
    
    win_combos = [[1,4,7], [2,5,8], [3,6,9], [1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7]]

    for combo in win_combos:
        check = all(board[num] == mark for num in combo)
        if check:
            return True

# win_check(test_board,'X')


import random

def choose_first():

    if random.randint(0, 1) == 0:
        print('Player 1 goes first') # should be return?
        return 'player1'
    else:
        print('Player 2 goes first') # should be return?
        return 'player2'

# choose_first()


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return all(position != ' ' for position in board)


def player_choice(board):

    choice = 0

    while choice not in range(1,10) or not space_check(board, choice):
        choice = int(input('Select your position (1-9) '))

    return int(choice)

def replay():

    response = 0

    while response != 'Y' and response != 'N':
        response = input('Play again? Y or N ').upper()

    if response == 'Y':
        return True
    else:
        return False


# SETTING UP THE GAME

replay_check = False

while True:

    ready = 0
    game_on = False
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    if not replay_check:
        while ready != 'Y' and ready != 'N':
            ready = input('Ready to play? Y or N ').upper()
        
        if ready == 'N':
            break
    
    game_on = True
    player1, player2 = player_input()
    current_player = choose_first()

    while game_on:

        if current_player == 'player1':
            display_board(board)
            num = player_choice(board)
            place_marker(board, player1, num)
            if win_check(board, player1):
                display_board(board)
                print('Player 1 wins!')
                break
            elif not win_check(board, player1) and full_board_check(board):
                display_board(board)
                print('Draw!')
                break
            else:
                current_player = 'player2'
        else:
            display_board(board)
            num = player_choice(board)
            place_marker(board, player2, num)
            if win_check(board, player2):
                display_board(board)
                print('Player 2 wins!')
                break
            elif not win_check(board, player2) and full_board_check(board):
                display_board(board)
                print('Draw!')
                break
            else:
                current_player = 'player1'

    replay_check = True  
    
    if not replay():
        break