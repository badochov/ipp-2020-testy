#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include "gamma.h"
#include <stdbool.h>
#include <string.h>


int main() {

/*
scenario: test_random_actions
uuid: 252457072
*/
/*
random actions, total chaos
*/
gamma_t* board = gamma_new(2, 3, 8, 7);
assert( board != NULL );


assert( gamma_move(board, 1, 0, 1) == 1 );
assert( gamma_move(board, 1, 0, 0) == 1 );
assert( gamma_move(board, 2, 1, 1) == 1 );
assert( gamma_move(board, 2, 0, 2) == 1 );
assert( gamma_move(board, 3, 0, 1) == 0 );
assert( gamma_free_fields(board, 3) == 2 );
assert( gamma_move(board, 5, 0, 1) == 0 );
assert( gamma_move(board, 5, 0, 2) == 0 );
assert( gamma_free_fields(board, 5) == 2 );
assert( gamma_move(board, 6, 2, 1) == 0 );
assert( gamma_busy_fields(board, 6) == 0 );
assert( gamma_move(board, 8, 2, 1) == 0 );
assert( gamma_move(board, 8, 1, 0) == 1 );
assert( gamma_move(board, 1, 0, 0) == 0 );
assert( gamma_golden_possible(board, 1) == 1 );
assert( gamma_move(board, 2, 2, 1) == 0 );
assert( gamma_move(board, 2, 1, 0) == 0 );
assert( gamma_move(board, 3, 2, 1) == 0 );
assert( gamma_move(board, 4, 2, 1) == 0 );


gamma_delete(board);

    return 0;
}
