from part1 import (
    gamma_board,
    gamma_busy_fields,
    gamma_delete,
    gamma_free_fields,
    gamma_golden_move,
    gamma_golden_possible,
    gamma_move,
    gamma_new,
)

"""
scenario: test_random_actions
uuid: 590594881
"""
"""
random actions, total chaos
"""
board = gamma_new(7, 4, 5, 4)
assert board is not None


assert gamma_move(board, 1, 2, 2) == 1 
assert gamma_move(board, 1, 1, 1) == 1 
assert gamma_golden_possible(board, 1) == 0 
assert gamma_move(board, 2, 5, 3) == 1 
assert gamma_busy_fields(board, 2) == 1 
assert gamma_golden_move(board, 2, 2, 2) == 1 
assert gamma_move(board, 3, 2, 1) == 1 
assert gamma_move(board, 4, 3, 1) == 1 
assert gamma_move(board, 4, 2, 0) == 1 
assert gamma_move(board, 5, 2, 2) == 0 
assert gamma_move(board, 1, 5, 3) == 0 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 2, 2, 3) == 1 
assert gamma_move(board, 2, 5, 0) == 1 
assert gamma_move(board, 3, 3, 2) == 1 
assert gamma_move(board, 3, 3, 0) == 1 
assert gamma_move(board, 4, 0, 1) == 1 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 5, 0, 1) == 0 
assert gamma_move(board, 1, 0, 6) == 0 
assert gamma_move(board, 2, 2, 6) == 0 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_busy_fields(board, 2) == 4 
assert gamma_golden_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 3, 6, 0) == 1 
assert gamma_free_fields(board, 3) == 4 
assert gamma_move(board, 4, 5, 2) == 1 
assert gamma_move(board, 5, 3, 4) == 0 
assert gamma_move(board, 5, 2, 1) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 2, 5, 1) == 1 
assert gamma_busy_fields(board, 2) == 5 
assert gamma_move(board, 4, 3, 2) == 0 
assert gamma_move(board, 4, 1, 3) == 0 
assert gamma_move(board, 5, 2, 4) == 0 
assert gamma_move(board, 5, 5, 3) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_busy_fields(board, 2) == 5 
assert gamma_move(board, 3, 5, 2) == 0 
assert gamma_move(board, 4, 3, 0) == 0 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 5, 5, 3) == 0 
assert gamma_golden_possible(board, 5) == 1 
assert gamma_move(board, 1, 1, 4) == 0 


board758376367 = gamma_board(board)
assert board758376367 is not None
assert board758376367 == ("..2..2.\n"
"..23.4.\n"
"4134.2.\n"
"..43.23\n")
del board758376367
board758376367 = None
assert gamma_busy_fields(board, 2) == 5 
assert gamma_move(board, 3, 4, 0) == 1 
assert gamma_move(board, 4, 0, 0) == 1 
assert gamma_busy_fields(board, 4) == 5 
assert gamma_golden_possible(board, 5) == 1 
assert gamma_move(board, 1, 4, 3) == 1 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_busy_fields(board, 2) == 5 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 3, 3, 1) == 0 
assert gamma_move(board, 4, 0, 0) == 0 
assert gamma_busy_fields(board, 4) == 5 
assert gamma_move(board, 5, 2, 6) == 0 
assert gamma_move(board, 5, 3, 0) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_move(board, 2, 2, 4) == 0 
assert gamma_move(board, 2, 6, 1) == 1 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 3, 3, 3) == 1 
assert gamma_move(board, 4, 4, 1) == 1 
assert gamma_move(board, 5, 3, 1) == 0 
assert gamma_move(board, 5, 6, 0) == 0 
assert gamma_move(board, 1, 3, 6) == 0 
assert gamma_move(board, 2, 6, 0) == 0 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 4, 3, 1) == 0 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 5, 3, 1) == 0 
assert gamma_move(board, 5, 4, 0) == 0 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 3, 5, 2) == 0 
assert gamma_move(board, 3, 5, 3) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 6, 0) == 0 
assert gamma_move(board, 4, 0, 2) == 1 
assert gamma_move(board, 5, 1, 0) == 1 
assert gamma_move(board, 5, 1, 3) == 1 
assert gamma_move(board, 1, 2, 6) == 0 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 2, 6, 1) == 0 
assert gamma_golden_move(board, 2, 1, 1) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 4, 2, 6) == 0 
assert gamma_move(board, 4, 4, 1) == 0 
assert gamma_move(board, 5, 2, 1) == 0 
assert gamma_golden_move(board, 5, 3, 4) == 0 
assert gamma_move(board, 1, 2, 1) == 0 


gamma_delete(board)
