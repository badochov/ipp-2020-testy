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
uuid: 629946632
"""
"""
random actions, total chaos
"""
board = gamma_new(5, 2, 2, 9)
assert board is not None


assert gamma_move(board, 1, 1, 4) == 0 
assert gamma_move(board, 1, 0, 1) == 1 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 1, 3, 1) == 1 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_move(board, 1, 1, 4) == 0 
assert gamma_move(board, 1, 3, 0) == 1 
assert gamma_busy_fields(board, 1) == 3 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 1, 4, 1) == 1 
assert gamma_move(board, 1, 2, 1) == 1 
assert gamma_move(board, 2, 2, 0) == 1 
assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_busy_fields(board, 1) == 6 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 2, 1, 0) == 1 
assert gamma_move(board, 1, 0, 4) == 0 
assert gamma_move(board, 1, 4, 1) == 0 
assert gamma_move(board, 2, 4, 1) == 0 
assert gamma_move(board, 1, 0, 4) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_free_fields(board, 2) == 1 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_busy_fields(board, 2) == 3 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 1, 0, 4) == 0 
assert gamma_free_fields(board, 1) == 1 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 4, 0) == 1 


board556809931 = gamma_board(board)
assert board556809931 is not None
assert board556809931 == ("12111\n"
"12212\n")
del board556809931
board556809931 = None


gamma_delete(board)