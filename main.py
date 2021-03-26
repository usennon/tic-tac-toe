from ai_player import minimax


def draw(board):
    board = board
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def win_check(board):
    for i in range(0, 6, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    for i in range(2):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True


def guess_input(symbol, board):
    while True:
        try:
            user_input = int(input('Choose a cell: '))
        except:
            print('Seems like you enter invalid information. Lets try again!')
        else:
            if user_input in range(1, 10) and board[user_input - 1] != 'X' \
                    and board[user_input - 1] != '0':
                board[user_input - 1] = f'{symbol}'
                return True
            else:
                print('You can not do that. Sell may not exist or there is already'
                      'exists.')


def game():
    turn = 0
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        human = False
        draw(board)
        turn += 1
        if turn % 2 != 0:
            human = guess_input('X', board)
        else:
            ai_guess = minimax(new_board, '0')
            board[int(ai_guess['index']) - 1] = '0'
            new_board = board
        if turn >= 3:
            if win_check(board) and human:
                print('Human win')
                draw(board)
                return 0
            elif win_check(board) and human == False:
                print('AI win')
                draw(board)
                return 0
        if turn == 9:
            print('It is a draw')
            draw(board)
            return 0


if __name__ == '__main__':
    game()
