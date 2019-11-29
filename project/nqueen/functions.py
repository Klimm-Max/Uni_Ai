def is_safe(board, n, r_idx, c_idx):
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
    board = [0] * n
    for i in range(n):
        board[i] = [0] * n
    return board


def print_board(board, n):
    print('_' * (2*n+1))
    for row in board:
        print('|' + '|'.join(str(x) for x in row).replace('0', ' ').replace('1', 'Q') + '|')
    print('\u203e' * (2 * n + 1))


def disable_unsafe_cells_in_board(board, n, row_idx, col_idx):
    # set all attacking positions from this queen on the upper-right diagonal
    i, j = row_idx, col_idx
    while i > 0 and j < n - 1:
        board[i-1][j+1] = -1
        i -= 1
        j += 1

    # set all attacking positions from the queen on the lower-right diagonal
    i, j = row_idx, col_idx
    while i < n - 1 and j < n - 1:
        board[i + 1][j + 1] = -1
        i += 1
        j += 1

    # calc all attacking positions in the same row (to the right)
    j = col_idx
    while j < n - 1:
        board[row_idx][j+1] = -1
        j += 1


def clear_board_from_attacks(board):
    for r_i, row in enumerate(board):
        for c_i, cell in enumerate(row):
            if cell == -1:
                board[r_i][c_i] = 0
