from board import *
from turn import *
from position_input import *
from rook import *
from bishop import *
from king import *
from pawn import *
from queen import *
from knight import *

init_grid()
print_grid()

input()

def move():
    Grid[fy][fx] == Grid[iy][ix]
    Grid[iy][ix] == '.'
    
if power == 'R' and validate_rook_move(start_pos, end_pos, Grid):
    move()
elif power == 'B' and validate_bishop_move(start_pos, end_pos, Grid):
    move()
elif power == 'H' and validate_knight_move(start_pos, end_pos, Grid):
    move()
elif power == 'Q' and validate_queen_move(start_pos, end_pos, Grid):
    move()
elif power == 'K' and validate_king_move(start_pos, end_pos, Grid):
    move()
elif power == 'P' and validate_pawn_move(start_pos, end_pos, Grid):
    move()