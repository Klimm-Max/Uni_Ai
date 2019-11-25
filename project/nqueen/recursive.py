import cProfile
from project.nqueen.api import is_safe, generate_empty_board, print_board


def solve(board, col):
    if col is n:                                    # this will only be reached if all queens have been placed and we
        print_board(board)                          # move to the outer of the chess
        return

    for row_idx in range(n):                        # for each row try to place the queens
        if is_safe(board, row_idx, col):
            board[row_idx][col] = 1
            if solve(board, col+1):                 # increase the column by 1 and try again to place all queens
                return True                         # this is very important because if there is no possible solution
        board[row_idx][col] = 0                     # the callee will return here and revert his placed queen

    return False


n = 10
cProfile.run('solve(generate_empty_board(n), 0)')
