# Create a Tic Tac Toe game
from __future__ import print_function
from IPython.display import clear_output
import random

def display_board(board):
    """Print out a board"""
    clear_output()

    for i, item in enumerate(board):
        if i in [2,5,8]:
            print(item)
        else:
            print(item, end=' ')

def player_input():
    """Take in a player input and assign their marker as 'X' or 'O'"""
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """Takes in the board list object 
    and assign the marker to the position on the board
    """
    board[position] = marker

def win_check(board,mark):
    """Checks to see if mark has won"""
    win_comb = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
        ]
    mark_pos = []
    for i, m in enumerate(board):
        if m == mark:
            mark_pos.append(i)
    for comb in win_comb:
        if set(comb) <= set(mark_pos):
            return True
    return False

def choose_first():
    """Randomly decide which player goes first"""
    first = random.randint(1,2)
    if first == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    """Check whether space on board is available and return a boolean value"""
    return board[position-1] not in ('X', 'O')

def full_board_check(board):
    """Checks if the board is full and return a boolean value"""
    for pos in board:
        if pos not in ('X', 'O'):
            return False
    return True

def player_choice(board):
    """Ask for a player's next position and check for free position
    and return the position for later use
    """
    pos = ' '
    while pos not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(pos)):
        pos = raw_input('Please input your next move (1-9): ')
    return int(pos) - 1

def replay():
    """Ask the player if they want to play again"""
    choice = raw_input('Play again(Y or N)? ')
    return choice.upper().startswith('Y')


print('Welcome to Tic Tac Toe!\n')

while True:
    (p1, p2) = player_input()
    theBoard = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    game_on = True
    turn = choose_first()
    print(turn + ' will go first')

    while game_on:
        if turn == 'Player 1':
            print("\nPlayer 1's Turn")
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, p1, position)
            if win_check(theBoard, p1):
                display_board(theBoard)
                print('Congrats You won the game\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie game\n')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            print("\nPlayer 2's Turn")
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, p2, position) 
            if win_check(theBoard, p2):
                display_board(theBoard)
                print('Congrats You won the game\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie game\n')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        print('Goodbye!')
        break                                   

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break



