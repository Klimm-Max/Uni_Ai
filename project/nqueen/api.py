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
    return [[0 for x in range(n)] for y in range(n)]


def print_board(board):
    # since the board is squared, we can just take the len of element 0
    n = len(board[0])

    print('_' * (2*n+1))
    for row in board:
        print('|' + '|'.join(str(x) for x in row).replace('0', ' ').replace('1', 'Q') + '|')
    print('\u203e' * (2 * n + 1))
