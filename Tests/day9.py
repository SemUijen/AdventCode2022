import numpy as np
from functions.day9_classes import Head, Tail
import copy
import sys
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)
from matplotlib import pyplot as plt

from IPython.display import display, HTML
def largest_grid_needed(lines):
    up = 0
    right = 0
    left = 0
    down = 0
    for line in lines:

        direction, steps = line.split()
        if direction == "R":
            right += int(steps)
        if direction == 'L':
            left += int(steps)

        if direction == "U":
            up += int(steps)
        if direction == 'D':
            down += int(steps)

    return np.zeros((2 * (up + down), (left + right)))


# what is going on with the lines textwrapper here? after looping through in function largest grid the other loop wont work anymore
def day9_part1():
    line1 = open('../data/day9_input.txt', 'r')
    lines = open('../data/day9_input.txt', 'r')
    Matrix = largest_grid_needed(lines)

    shape = Matrix.shape
    starting_position = (round(shape[0] / 2), round(shape[1] / 2))
    Matrix[starting_position] = 1

    head = Head(0,starting_position[1], starting_position[0],
                Tail(1, starting_position[1], starting_position[0], Matrix, None))

    for line in line1:
        direction, steps = line.split()
        head.move(direction=direction, steps=int(steps))


    return head.tail.matrix.sum()


def day9_part2():
    line1 = open('../data/day9_input.txt', 'r')
    lines = open('../data/day9_input.txt', 'r')
    Matrix = largest_grid_needed(lines)

    shape = Matrix.shape
    starting_position = (round(shape[0] / 2), round(shape[1] / 2))
    Matrix[starting_position] = 1
    print(starting_position)
    head = Head(0,starting_position[1], starting_position[0],
                Tail(1, starting_position[1], starting_position[0], None,
                     Tail(2, starting_position[1], starting_position[0], None,
                          Tail(3, starting_position[1], starting_position[0], None,
                               Tail(4, starting_position[1], starting_position[0], None,
                                    Tail(5, starting_position[1], starting_position[0], None,
                                         Tail(6, starting_position[1], starting_position[0], None,
                                              Tail(7, starting_position[1], starting_position[0], None,
                                                   Tail(8, starting_position[1], starting_position[0], None,
                                                        Tail(9, starting_position[1], starting_position[0], Matrix, None))))))))))


    for line in line1:
        direction, steps = line.split()
        head.move(direction=direction, steps=int(steps))

    # print(head.tail.matrix.sum())
    # print(head.find_tail().matrix)
    x = head.find_tail().matrix
    plt.imshow(x, interpolation='nearest')
    plt.show()
    return x.sum()



print(day9_part2())


