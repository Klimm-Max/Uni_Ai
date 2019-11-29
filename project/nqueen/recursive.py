import cProfile
from project.nqueen.api import is_safe, generate_empty_board, print_board


def solve(board, n, col_idx):
    if col_idx is n:                                    # this will only be reached if all queens have been placed and we
        print_board(board, n)                           # move to the outer of the chess
        return

    for row_idx in range(n):                            # for each row try to place the queens
        if is_safe(board, n, row_idx, col_idx):
            board[row_idx][col_idx] = 1
            if solve(board, n, col_idx + 1):            # increase the column by 1 and try again to place all queens
                return True                             # this is important because if there is no possible solution
        board[row_idx][col_idx] = 0                     # the callee will return here and revert his placed queen

    return False


dimension = 10
brd = generate_empty_board(dimension)
cProfile.run('solve(bo, dimension, 0)')
