lines = open('../data/day8_test.txt', 'r')
import numpy as np
import re
def build_matrix():
    temp_matrix = []
    for line in lines:
        line = line.replace('\n', '')

        map1 = map(int, line)
        temp_matrix.append(list(map1))
    array = np.array(temp_matrix)
    return array

def day1_part1():
    tree_matrix = build_matrix()
    visibleTree_matrix = np.zeros(tree_matrix.shape)
    score = 0
    for position, tree in np.ndenumerate(tree_matrix):

        if position[0] in [0, tree_matrix.shape[0]-1] or position[1] in [0, tree_matrix.shape[1]-1]:
            score += 1


#test
    return score
print(day1_part1())



