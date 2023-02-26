def validate_rook_move(start_pos, end_pos, board):

    if start_pos == end_pos:
        return False

    
    if start_pos[0] != end_pos[0] and start_pos[1] != end_pos[1]:
        return False
    
    
    if start_pos[0] == end_pos[0]:  
        start_col = min(start_pos[1], end_pos[1])
        end_col = max(start_pos[1], end_pos[1])
        for col in range(start_col+1, end_col):
            if board[start_pos[0]][col] != '.':
                return False
    else:  
        start_row = min(start_pos[0], end_pos[0])
        end_row = max(start_pos[0], end_pos[0])
        for row in range(start_row+1, end_row):
            if board[row][start_pos[1]] != '.':
                return False
    
    
    return True
