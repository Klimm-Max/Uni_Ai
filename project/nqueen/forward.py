import cProfile
from project.nqueen.api import *


def solve(board, n, col_idx):
    if col_idx is n:
        clear_board_from_attacks(board)
        print_board(board, n)
        return

    for row_idx in range(n):
        if board[row_idx][col_idx] != -1 and is_safe(board, n, row_idx, col_idx):
            board[row_idx][col_idx] = 1
            disable_unsafe_cells_in_board(board, n, row_idx, col_idx)
            if solve(board, n, col_idx + 1):
                return True

        board[row_idx][col_idx] = 0                             # disabled cells will be resolved here as well

    return False


dimension = 10
brd = generate_empty_board(dimension)
cProfile.run('solve(brd, dimension, 0)')
