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
uuid: 294256464
"""
"""
random actions, total chaos
"""
board = gamma_new(4, 2, 4, 1)
assert board is not None


assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_move(board, 2, 0, 3) == 0 
assert gamma_move(board, 2, 2, 0) == 1 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_move(board, 4, 1, 2) == 0 
assert gamma_move(board, 4, 1, 1) == 1 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 2, 0, 3) == 0 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 1, 3) == 0 
assert gamma_golden_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_busy_fields(board, 3) == 1 
assert gamma_golden_move(board, 3, 0, 0) == 1 


board265159643 = gamma_board(board)
assert board265159643 is not None
assert board265159643 == ("34..\n"
"3.2.\n")
del board265159643
board265159643 = None
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 3, 0, 1) == 0 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 4, 0, 0) == 0 
assert gamma_busy_fields(board, 4) == 1 


gamma_delete(board)