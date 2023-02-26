def init_grid():

    global Grid

    Grid = [['.' for i in range(8)] for j in range(8)]
    posti=['R','H','B','Q','K','B','H','R']
    for i in range(8):
        Grid[0][i] = 'B' + posti[i]
    for i in range(8):
        Grid[-1][i] = 'W' + posti[i]
    for i in range(8):
        Grid[1][i] = 'BP'
    for i in range(8):
        Grid[-2][i] = 'WP'

def print_grid():
    global Grid
    for i in Grid:
        print(i)

init_grid()