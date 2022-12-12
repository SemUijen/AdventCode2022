import numpy as np
import re

lines = open('../data/day8_input.txt', 'r')


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

    score = 0
    for position, tree in np.ndenumerate(tree_matrix):

        if position[0] in [0, tree_matrix.shape[0] - 1] or position[1] in [0, tree_matrix.shape[1] - 1]:
            score += 1
            continue

        else:
            if all(tree > tree_matrix[position[0]][0:position[1]]) or all(
                    tree > tree_matrix[position[0]][position[1] + 1:tree_matrix.shape[1]]):
                score += 1


            else:

                above_tree = [tree > tree_matrix[i][position[1]] for i in range(0, position[0])]

                below_tree = [tree > tree_matrix[i][position[1]] for i in range(position[0] + 1, tree_matrix.shape[0])]

                if all(above_tree) or all(below_tree):
                    score += 1

    return score


def day1_part2():
    tree_matrix = build_matrix()
    visibleTree_matrix = np.zeros(tree_matrix.shape)
    best_score = 0
    for position, tree in np.ndenumerate(tree_matrix):
        left = 0
        right = 0
        above = 0
        below = 0
        if position[0] in [0, tree_matrix.shape[0] - 1] or position[1] in [0, tree_matrix.shape[1] - 1]:
            continue

        for i in reversed(range(0, position[0])):

            if tree > tree_matrix[i][position[1]]:
                above += 1
            else:
                above += 1
                break

        for i in range(position[0] + 1, tree_matrix.shape[0]):
            if tree > tree_matrix[i][position[1]]:
                below += 1
            else:
                below += 1
                break

        for i in reversed(range(0, position[1])):

            if tree > tree_matrix[position[0]][i]:
                left += 1
            else:
                left += 1
                break

        for i in range(position[1] + 1, tree_matrix.shape[1]):
            if tree > tree_matrix[position[0]][i]:
                right += 1
            else:
                right += 1
                break

        new_score = left * right * above * below
        if new_score > best_score:

            best_score = new_score

    return best_score


print(day1_part2())
