def validate_queen_move(start_pos, end_pos, board):
    
    if start_pos == end_pos:
        return False
    

    if abs(end_pos[0] - start_pos[0]) == abs(end_pos[1] - start_pos[1]):
        
        row_step = 1 if end_pos[0] > start_pos[0] else -1
        col_step = 1 if end_pos[1] > start_pos[1] else -1
        row, col = start_pos
        while row != end_pos[0] and col != end_pos[1]:
            row += row_step
            col += col_step
            if board[row][col] != '.':
                return False
        return True
    
   
    if start_pos[0] == end_pos[0]:  
        start_col = min(start_pos[1], end_pos[1])
        end_col = max(start_pos[1], end_pos[1])
        for col in range(start_col+1, end_col):
            if board[start_pos[0]][col] != '.':
                return False
        return True
    elif start_pos[1] == end_pos[1]: 
        start_row = min(start_pos[0], end_pos[0])
        end_row = max(start_pos[0], end_pos[0])
        for row in range(start_row+1, end_row):
            if board[row][start_pos[1]] != '.':
                return False
        return True
    
    
    return False
