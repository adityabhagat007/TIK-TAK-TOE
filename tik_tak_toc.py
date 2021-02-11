
import random


def display_board(board):

    print('\n'*100)
    print('  |  |  ')
    print(board[1] + ' |' + board[2] + ' |' + board[3])
    print('  |  |  ')
    print('--------')
    print('  |  |  ')
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print('  |  |  ')
    print('--------')
    print('  |  |  ')
    print(board[7] + ' |' + board[8] + ' |' + board[9])
    print('  |  |  ')


def player_input():

    choice='wrong'
    while choice.isdigit() == False:

        choice=input('Enter the Position (1-9):-')
        if choice.isdigit() == False:

           print('Enter in digit format')
    return choice


def select_process():
    print('select the symbols between X and O')
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input('player please enter the symbol X or O').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_maker(board,marker,position):
    board[position]=marker

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def win_check(board,marker):

    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker)or
            (board[3] == marker and board[5] == marker and board[7] == marker)or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker))


def space_check(board ,position):
    return board[position] == ' '


def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position= int(input('Choose your next position: (1-9)'
                            ':- '))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


b1=['0','1','2','3','4','5','6','7','8','9']
display_board(b1)
print("WElCOME to the GAME LET'S PLAY")
print('remember the board model')


while True:

    b = [' ']*10

    ply1,ply2 = select_process()
    turn = choose_first()
    print(turn + ' will start first')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn=='Player 1':
            display_board(b)
            player = player_choice(b)
            place_maker(b,ply1,player)

            if win_check(b, ply1):
                display_board(b)
                print('Congratulations! player1 You have won the game!')
                game_on = False

            else:
                if fullboard_check(b):
                    display_board(b)
                    print('Draw game')
                    break
                else:
                    display_board(b)
                    turn= 'Player 2'

        else:

            if turn == 'Player 2' :
                display_board(b)
                player = player_choice(b)
                place_maker(b, ply2, player)
                display_board(b)

                if win_check(b, ply2):
                    display_board(b)
                    print('Congratulations! player2 You have won the game!')
                    game_on = False

                else:
                    if fullboard_check(b):
                        display_board(b)
                        print('Draw game')
                        break
                    else:
                        display_board(b)
                        turn = 'Player 1'
    if not replay():
        break































