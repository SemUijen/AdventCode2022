lines = open('../data/day6_input.txt', 'r')

def day6_part1():
    line = lines.readline()
    for i in range(len(line)-4):
        x = line[i:i+4]
        if len(set(x)) == 4:
            return i+4


def day6_part2():
    line = lines.read()
    for i in range(len(line)-14):
        x = line[i:i+14]
        if len(set(x)) == 14:
            return i+14
