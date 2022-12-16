import matplotlib.pyplot as plt
import numpy as np

from functions.Classes_day10 import Sprite

lines = open('../data/day10_input.txt', 'r')


def day10_part1():
    signal_list = []
    single_register = 1
    signal_strength = 0
    cycle = 0
    max_cycles = 0
    for line in lines:

        if line[0:4] == 'noop':
            max_cycles += 1
            signal_list.insert(0, 0)
        if line[0:4] == 'addx':
            max_cycles += 2
            _, value = line.split()
            signal_list.insert(0, 0)
            signal_list.insert(0, int(value))

    for cycle in range(1, max_cycles + 1):

        if cycle in [*range(20, max_cycles, 40)]:
            signal_strength += single_register * cycle

        single_register += signal_list.pop()
    print(max_cycles)
    return signal_strength




def day10_part2():
    signal_list = []
    single_register = 1
    signal_strength = 0
    cycle = 0
    max_cycles = 0
    for line in lines:

        if line[0:4] == 'noop':
            max_cycles += 1
            signal_list.insert(0, 0)
        if line[0:4] == 'addx':
            max_cycles += 2
            _, value = line.split()
            signal_list.insert(0, 0)
            signal_list.insert(0, int(value))

    Matrix = []
    temp_list = []
    temp_cycle = 0
    sprite = Sprite(0, 1, 2)

    for cycle in range(1, max_cycles + 1):
        if temp_cycle in sprite.pos_list():
            temp_list.append(1)
        if temp_cycle not in sprite.pos_list():
            temp_list.append(0)

        sprite.change_position(signal_list.pop())
        temp_cycle += 1

        if temp_cycle == 40:
            Matrix.append(temp_list)
            temp_list = []
            temp_cycle = 0

    x = np.array(Matrix)
    print(x)
    plt.imshow(x, interpolation='nearest')
    plt.show()


print(day10_part2())
