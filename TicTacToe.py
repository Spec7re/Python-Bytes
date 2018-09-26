from IPython.display import clear_output

def display_board(board):
    clear_output()
    """ prints the tic-tac-toe board"""
    print(" +---1------2------3--+")
    print(" |      |      |      |")
    print(" |  " + board[1] +"   |  " + board[2] +"   |  " + board[3] + "   |")
    print(" |      |      |      |")
    print(" +--------------------+")
    print(" |      |      |      |")
    print("4|  " + board[4] +"   |  " + board[5] +"   |  " + board[6] + "   |6")
    print(" |      |      |      |")
    print(" +--------------------+")
    print(" |      |      |      |")
    print(" |  " + board[7] +"   |  " + board[8] +"   |  " + board[9] + "   |")
    print(" |      |      |      |")
    print(" +---7------8------9--+")


def player_input():
    marker = ""
    while not (marker == 'X' or marker == 'O'):
          marker = input("Pick marker X or O : ").upper()
    if marker == 'X':
        return ('X','O')
    else: 
        return ('O','X')


def place_marker(board, marker, position):
    x = int(position)
    board[x] = marker


def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[5]==board[9]==mark) or 
    (board[3]==board[5]==board[7]==mark))


import random

def choose_first():
    if random.randint(0,1) == 0:
        print ("Player 1")
        return 0
    else:
        print ("Player 2")
        return 1
        

def space_check(board, position):
     return board[position] == ' '


def player_choice(board):
    position = ' '
    while position not in [1,2,3,4,5,6,7,8,9] or space_check(board, position) != True:
        position = int(input('Number 1-9 or New position:'))
    
#     while 
#         position = int(input('Already assigned postiion :'))     
    return position 

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def replay():
    answer = ' '
    while not (answer == 'Y' or answer == 'N'):
        answer = input("Do you want to play again Y or N? ").upper()
    if answer == 'Y':
        return True
    else:
        return False


def clearBoard(board):
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board


boardPlay = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


print('Welcome to Tic Tac Toe!')

board = boardPlay

result = input('Ready to Play Y or N :').upper()

if result == 'Y':
    gameOn = True
    board = clearBoard(boardPlay)
else:
    gameOn = False
#Who is first    
turn = choose_first()
#Choose marker
marker = player_input()
#while True:
while gameOn:
    # Set the game up here
    display_board(board)
    if turn == 0:            
        #Player 1 Turn
        position = player_choice(board)
        mark = marker[0]
        place_marker(board, mark, position)
        turn = 1
        #Checks for Win
        if win_check(board, mark) == True:
            print(f'Player - {mark} - wins!')
            if replay() == True:
                gameOn = True
                board = clearBoard(boardPlay)
            else:
                break            
        #Checks for FullBoard    
        if full_board_check(board) == True:
            print('Game Over')
            if replay() == True:
                gameOn = True
                board = clearBoard(boardPlay)
            else:
                break      
    else:
        # Player2's turn.
        position = player_choice(board)
        mark = marker[1]
        place_marker(board, mark, position)
        turn = 0
        # Checks for Win
        if win_check(board, mark) == True:
            print(f'Player - {mark} - wins!')
            if replay() == True:
                gameOn = True
                board = clearBoard(boardPlay)
            else:
                break       
        # Checks for FullBoard
        if full_board_check(board) == True:
            print('Game Over')
            if replay() == True:
                gameOn = True
                board = clearBoard(boardPlay)
            else:
                break           