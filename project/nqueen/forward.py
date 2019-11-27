import cProfile
from project.nqueen.api import generate_empty_board, clear_board_from_attacks, \
    print_board, is_safe, disable_unsafe_cells_in_board


def solve(board, n, col_idx):
    if col_idx is n:
        clear_board_from_attacks(board)
        print_board(board)
        return

    for row_idx in range(n):
        if board[row_idx][col_idx] != -1 and is_safe(board, row_idx, col_idx):  # unsafe cells from previous placements
            board[row_idx][col_idx] = 1
            disable_unsafe_cells_in_board(board, row_idx, col_idx)              # all unsafe cells from this queen = -1
            if solve(board, n, col_idx + 1):
                return True

        board[row_idx][col_idx] = 0                             # disabled cells by setting all their values to 0 again

    return False


dimension = 12
cProfile.run('solve(generate_empty_board(dimension), dimension, 0)')
"""
29 699 376 function calls (28888680 primitive calls) in 40.713 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   40.713   40.713 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 api.py:32(generate_empty_board)
  5349661   23.184    0.000   23.426    0.000 api.py:4(is_safe)
     4896    0.073    0.000    0.878    0.000 api.py:44(print_board)
   763776    0.448    0.000    0.448    0.000 api.py:50(<genexpr>)
   810696    3.519    0.000    7.909    0.000 api.py:54(remove_all_attacks)
   810696    3.479    0.000    3.909    0.000 api.py:68(get_all_attacking_moves)
     4896    0.266    0.000    0.266    0.000 api.py:93(clear_board_from_attacks)
 810697/1    8.235    0.000   40.713   40.713 forward.py:5(solve)
        1    0.000    0.000   40.713   40.713 {built-in method builtins.exec}
  6165253    0.280    0.000    0.280    0.000 {built-in method builtins.len}
    68544    0.253    0.000    0.253    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
  7367000    0.430    0.000    0.430    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    58752    0.081    0.000    0.529    0.000 {method 'join' of 'str' objects}
  7367000    0.442    0.000    0.442    0.000 {method 'keys' of 'dict' objects}
   117504    0.022    0.000    0.022    0.000 {method 'replace' of 'str' objects}
"""

"""
=========================== RECURSIVE =====================================
   2 4017 530 function calls (23161342 primitive calls) in 47.140 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   47.140   47.140 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 api.py:32(generate_empty_board)
 10103868   39.732    0.000   40.164    0.000 api.py:4(is_safe)
    14200    0.204    0.000    2.528    0.000 api.py:44(print_board)
  2215200    1.304    0.000    1.304    0.000 api.py:50(<genexpr>)
 856189/1    4.448    0.000   47.140   47.140 recursive.py:5(solve)
        1    0.000    0.000   47.140   47.140 {built-in method builtins.exec}
 10118068    0.432    0.000    0.432    0.000 {built-in method builtins.len}
   198800    0.734    0.000    0.734    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   170400    0.227    0.000    1.531    0.000 {method 'join' of 'str' objects}
   340800    0.059    0.000    0.059    0.000 {method 'replace' of 'str' objects}
"""