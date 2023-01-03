import re
import numpy as np
lines = open('../data/Day14_test.txt', 'r')
rock_traces = lines.read().strip().split('\n')


def create_matrix():
    lowest_point = 1
    furthest_r = 0
    furthest_l = 0
    for rock in rock_traces:
        rock_trace = re.split('->', rock)
        print(rock_trace)

    # STARTING POSITION NEEDS TO BE DEFINED: 500,0 is starting position but 500 will not exist in matrix
    start_pos_sand = (0,0)
    # size of 5,5 ALSO NEEDS TO BE CHANGED WHEN LOOP IS FINISHED
    Matrix = np.full((5,5),0)
    #all position in matrix that have a rock (CHANGE THIS TO ACTUAL POSITIONS)
    rock_positions = [start_pos_sand,(0,2)]
    # set values of matrix to 1
    np.put(Matrix,rock_positions,1)
    return Matrix, lowest_point, start_pos_sand

matrix, _,_,_ = create_matrix()
print(matrix)