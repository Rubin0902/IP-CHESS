def validate_bishop_move(start_pos, end_pos, board):

    if start_pos == end_pos:
        return False


    if abs(start_pos[0] - end_pos[0]) != abs(start_pos[1] - end_pos[1]):

        return False
    

    delta_row = 1 if end_pos[0] > start_pos[0] else -1
    delta_col = 1 if end_pos[1] > start_pos[1] else -1
    row, col = start_pos[0] + delta_row, start_pos[1] + delta_col
    while row != end_pos[0] and col != end_pos[1]:
        if board[row][col] != '.':
            return False
        row += delta_row
        col += delta_col
    

    return True