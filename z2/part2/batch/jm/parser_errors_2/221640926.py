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
uuid: 221640926
"""
"""
random actions, total chaos
"""
board = gamma_new(3, 2, 3, 1)
assert board is not None


assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 1 


board292956033 = gamma_board(board)
assert board292956033 is not None
assert board292956033 == ("2..\n"
".1.\n")
del board292956033
board292956033 = None
assert gamma_move(board, 3, 1, 1) == 1 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 1, 2, 0) == 1 


board285727616 = gamma_board(board)
assert board285727616 is not None
assert board285727616 == ("23.\n"
".11\n")
del board285727616
board285727616 = None
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_busy_fields(board, 2) == 2 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_busy_fields(board, 3) == 1 
assert gamma_golden_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 1, 1, 2) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_free_fields(board, 2) == 0 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_busy_fields(board, 3) == 1 


gamma_delete(board)