import position_input

move_num = 0

def get_turn(move_num):
    if move_num % 2 == 0:
        return 'White'
    else:
        return 'Black'
    
def validate_turn():
    if get_turn(move_num) == position_input.colour :
        return True