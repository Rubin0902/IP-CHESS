def validate_knight_move(start_pos, end_pos):

    if start_pos == end_pos:
        return False
    

    row_diff = abs(start_pos[0] - end_pos[0])
    col_diff = abs(start_pos[1] - end_pos[1])
    if not ((row_diff == 1 and col_diff == 2) or
            (row_diff == 2 and col_diff == 1)):
        return False
    

    return True
