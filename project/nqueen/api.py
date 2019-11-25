import numpy


def is_safe(board, r_idx, c_idx):
    # since the board is squared, we can just take the len of element 0
    n = len(board[0])

    # check if there is any Queen on the same row
    for i in range(c_idx):
        if board[r_idx][i] == 1:
            return False

    # checking all upper-left diagonals until we reach the border
    i, j = r_idx, c_idx
    while i > 0 and j > 0:
        if board[i - 1][j - 1] == 1:
            return False
        i -= 1
        j -= 1

    # check all lower-left diagonals until we reach the bottom border
    i, j = r_idx, c_idx
    while i < n-1 and j > 0:
        if board[i + 1][j - 1] == 1:
            return False
        i += 1
        j -= 1

    return True


def generate_empty_board(n):
    return numpy.zeros((n, n), numpy.int32)


def generate_all_coordinates(n):
    coords = []
    for rows in range(n):
        for columns in range(n):
            coords.append(dict([(rows, columns)]))
    return coords


def print_board(board):
    # since the board is squared, we can just take the len of element 0
    n = len(board[0])

    print('_' * (2*n+1))
    for row in board:
        print('|' + '|'.join(str(x) for x in row).replace('0', ' ').replace('1', 'Q') + '|')
    print('\u203e' * (2 * n + 1))


def disable_unsafe_cells_in_board(board, row_idx, col_idx):
    n = len(board[0])
    for attack in get_all_attacking_moves(n, row_idx, col_idx):
        for k in attack.keys():
            board[k][attack[k]] = -1


def get_all_attacking_moves(n, row_idx, col_idx):
    attacking_moves = []

    # remove all attacking positions from the queen on the upper-right diagonal
    i, j = row_idx, col_idx
    while i > 0 and j < n-1:
        attacking_moves.append(dict([(i-1, j+1)]))
        i -= 1
        j += 1

    # remove all attacking positions from the queen on the lower-right diagonal
    i, j = row_idx, col_idx
    while i < n - 1 and j < n - 1:
        attacking_moves.append(dict([(i + 1, j + 1)]))
        i += 1
        j += 1

    # remove all attacking positions in the same row (to the right)
    j = col_idx
    while j < n - 1:
        attacking_moves.append(dict([(row_idx, j+1)]))
        j += 1

    return attacking_moves


def clear_board_from_attacks(board):
    for r_i, row in enumerate(board):
        for c_i, cell in enumerate(row):
            if cell == -1:
                board[r_i][c_i] = 0
