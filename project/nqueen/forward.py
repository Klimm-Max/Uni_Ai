import cProfile
from project.nqueen.api import *


def solve(board, n, col_idx):
    """this approach got improved since placing a queen will lead to disabling all here attacking moves
    which reduces the number of iterations"""
    if col_idx is n:
        print_board(board)
        return

    for row_idx in range(n):
        if board[row_idx][col_idx] is not False and is_safe(board, row_idx, col_idx):
            board[row_idx][col_idx] = 1
            remove_all_attacks(board, row_idx, col_idx)     # setting all the attack moves of the current queen in the
            if solve(board, n, col_idx + 1):                # board to False and check in the next iteration
                return True

        add_all_attacks(board, row_idx, col_idx)            # in the backtracking, we need to restore the previously
        board[row_idx][col_idx] = 0                         # disabled cells by setting all their values to 0 again

    return False


dimension = 10
cProfile.run('solve(generate_empty_board(dimension), dimension, 0)')
