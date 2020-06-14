from IPython.display import clear_output
import random

def display_board(board):
    
    clear_output()
    
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
    
def player_input():
 
    marker = ' '
    
    
    
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, please pick a marker: 'X' or 'O'. ")
        
    
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[7] == mark and mark == board[8] and mark == board[9]:
        return True
    elif mark == board[4] and mark == board[5] and mark == board[6]:
        return True
    elif mark == board[7] and mark == board[2] and mark == board[3]:
        return True
    elif mark == board[7] and mark == board[4] and mark == board[1]:
        return True
    elif mark == board[8] and mark == board[5] and mark == board[2]:
        return True
    elif mark == board[9] and mark == board[6] and mark == board[3]:
        return True
    elif board[7] == mark and board[5] == mark and mark == board[3]:
        return True
    elif mark == board[9] and mark == board[5] and mark == board [1]:
        return True
    else:
        return False
    
   

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'
        
def space_check(board, position):
    
    return board[position] == ' '
    
def full_board_check(board):
    for num in range(1,10):
        if space_check(board, num):
            return True
        else:
            False
        
def player_choice(board):

    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
        
        
    return position


def replay():
    response =  input('Do you want to play again? Answer Yes or No.')
    if response == 'Yes':
        return True
    else:
        return False
        
#Functions for code below:


print('Welcome to Tic Tac Toe! Everything is case sensitive')

while True:
    
    theBoard = [' '] * 10
    player1marker, player2marker = player_input() 
    print('\nPlayer 1, your marker is '+ player1marker + '.')
    print('Player 2, your marker is '+ player2marker + '.')
    turn = choose_first()
    print("\n" + turn + ', you are going first!')
    
    
    playgame = input('Are you ready to start the game? Enter Yes or No:')
    
    if playgame == 'Yes':
        game_on = True
    else: 
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1marker, position)
           
            if win_check(theBoard, player1marker):
                display_board(theBoard)
                print('Congrats Player 1, you have won!')
                game_on = False
                
            else:
                if not full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(theBoard)
            position = player_choice(theBoard) 
            place_marker(theBoard, player2marker, position)
                
            if win_check(theBoard, player2marker):
                display_board(theBoard)
                print('Congrats Player 2, you have won!')
                game_on = False
                        
            else:
                if not full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE GAME!')
                    game_on = False
        
                else:
                    turn = 'Player 1'
                
            
       
            
            
            
        
        
        
        
    
            
            
        
    if replay():
        continue
    else:
        break
