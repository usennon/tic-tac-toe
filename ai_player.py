def emptyIndices(board):
    return [board.index(item) for item in board if item != 'X' and item != '0']


def winning(board, player):
    if board[0] == player and board[1] == player and board[2] == player or \
            board[3] == player and board[4] == player and board[5] == player or \
            board[6] == player and board[7] == player and board[8] == player or \
            board[0] == player and board[3] == player and board[6] == player or \
            board[1] == player and board[4] == player and board[7] == player or \
            board[2] == player and board[5] == player and board[8] == player or \
            board[0] == player and board[4] == player and board[8] == player or \
            board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False


def minimax(new_board, player):
    huPlayer = 'X'
    aiPlayer = '0'
    availSpots = emptyIndices(new_board)
    if winning(new_board, huPlayer):
        return {"score": -10}
    elif winning(new_board, aiPlayer):
        return {"score": +10}
    elif len(availSpots) == 0:
        return {"score": 0}

    moves = []

    for i in range(0, len(availSpots)):
        move = {}
        move['index'] = new_board[availSpots[i]]

        new_board[availSpots[i]] = player

        if player == aiPlayer:
            result = minimax(new_board, huPlayer)
            move['score'] = result['score']
        else:
            result = minimax(new_board, aiPlayer)
            move['score'] = result['score']

        new_board[availSpots[i]] = move['index']

        moves.append(move)

    best_move = 0
    if player == aiPlayer:
        best_score = -10000
        for j in range(0, len(moves)):
            if moves[j]['score'] > best_score:
                best_score = moves[j]['score']
                best_move = j
        return moves[best_move]
    else:
        best_score = 10000
        for j in range(0, len(moves)):
            if moves[j]['score'] < best_score:
                best_score = moves[j]['score']
                best_move = j

        return moves[best_move]

