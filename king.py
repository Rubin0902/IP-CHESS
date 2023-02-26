def validate_king_move( start_pos, end_pos, board):

    if start_pos == end_pos:
        return False
    
    if abs(start_pos[0] - end_pos[0]) > 1 or abs(start_pos[1] - end_pos[1]) > 1:
        return False
    
    
    if board[end_pos[0]][end_pos[1]].islower() == board[start_pos[0]][start_pos[1]].islower():
        return False
    
    return True