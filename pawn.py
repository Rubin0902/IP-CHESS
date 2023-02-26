from turn import get_turn 

def validate_pawn_move(start_pos, end_pos, board):

    if start_pos == end_pos:
        return False

    row_diff = end_pos[0] - start_pos[0]
    col_diff = end_pos[1] - start_pos[1]

    if get_turn() == 'White':

        if row_diff == -1 and abs(col_diff) == 1:  

            if board[end_pos[0]][end_pos[1]] != '.' and board[end_pos[0]][end_pos[1]][0] == 'B':
                return True
            

        elif row_diff == -1 and col_diff == 0:  

            if board[end_pos[0]][end_pos[1]] == '.':
                return True
            

        elif row_diff == -2 and col_diff == 0 and start_pos[0] == 6:  
            if board[end_pos[0]][end_pos[1]] == '.' and board[end_pos[0]+1][end_pos[1]] == '.':
                return True


    else:  

        if row_diff == 1 and abs(col_diff) == 1:  

            if board[end_pos[0]][end_pos[1]] != '.' and board[end_pos[0]][end_pos[1]][0] == 'W':
                return True


        elif row_diff == 1 and col_diff == 0:  
            
            if board[end_pos[0]][end_pos[1]] == '.':
                return True


        elif row_diff == 2 and col_diff == 0 and start_pos[0] == 1: 
            
            if board[end_pos[0]][end_pos[1]] == '.' and board[end_pos[0]-1][end_pos[1]] == '.':
                return True


    return False
