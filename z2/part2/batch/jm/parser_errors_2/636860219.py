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
uuid: 636860219
"""
"""
random actions, total chaos
"""
board = gamma_new(2, 5, 3, 2)
assert board is not None


assert gamma_move(board, 1, 0, 3) == 1 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_busy_fields(board, 2) == 0 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 3, 2, 0) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 2, 1, 0) == 1 
assert gamma_move(board, 3, 2, 0) == 0 
assert gamma_move(board, 3, 1, 2) == 1 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 2, 1, 0) == 0 


board856890678 = gamma_board(board)
assert board856890678 is not None
assert board856890678 == ("..\n"
"1.\n"
".3\n"
".2\n"
".2\n")
del board856890678
board856890678 = None
assert gamma_move(board, 3, 0, 0) == 1 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 3, 4, 1) == 0 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 1, 0, 4) == 1 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 2, 2, 0) == 0 


gamma_delete(board)
