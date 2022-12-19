import string
import re
import numpy as np
from functions.class_12 import Path

lines = open('../data/Day12_input.txt', 'r')



def Get_matrix():
    input_list = []
    i = 0
    for line in lines:
        row = re.findall('[a-zA-Z]', line)
        if 'S' in row:
            starting_position = (i, row.index('S'))
        if 'E' in row:
            ending_position = (i, row.index('E'))

        list = [ord(char) - 96 for char in row]

        input_list.append(list)
        i += 1

    input_matrix = np.array(input_list)
    input_matrix[starting_position] = 0
    input_matrix[ending_position] *= -1
    path_matrix = np.full(input_matrix.shape, input_matrix.shape[0] * input_matrix.shape[1])

    return starting_position, ending_position, input_matrix, path_matrix


def day12_part1():
    starting_pos, ending_position, input_matrix, path_matrix = Get_matrix()
    path = Path(1, path_matrix, input_matrix, starting_pos[1], starting_pos[0])
    path.walk()

    print(path_matrix)
    print(path.shortest_path)





def day12_part2():
    starting_pos, ending_pos, input_matrix, path_matrix = Get_matrix()
    path = Path(1, path_matrix, input_matrix, ending_pos[1], ending_pos[0])
    path.reverese_walk()

    print(input_matrix)
    print(path_matrix)
    print(path.shortest_path_A)

day12_part2()

