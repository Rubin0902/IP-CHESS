from board import *

global ix,iy,fx,fy,start_pos,end_pos 

def input():

    global ix,iy,fx,fy,start_pos,end_pos 
    
    ix=int(input('Enter the intial X position'))
    iy=int(input('Enter the intial Y position'))

    start_pos=[iy,ix]

    fx=int(input('Enter the final X position'))
    fy=int(input('Enter the final Y position'))

    end_pos=[fy,fx]

colour=Grid[start_pos[0]][start_pos[1]][0]
power=Grid[start_pos[0]][start_pos[1]][1]