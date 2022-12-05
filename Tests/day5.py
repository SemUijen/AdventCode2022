lines = open('../data/day5_input.txt', 'r')

test_dict = {1: ['N', 'Z'], 2: ['D', 'C', 'M'], 3: ['P']}
input_dict = {1: ['L', 'C', 'G', 'M', 'Q'], 2: ['G', 'H', 'F', 'T', 'C', 'L', 'D', 'R'],
              3: ['R', 'W', 'T', 'M', 'N', 'F', 'J', 'V'],
              4: ['P', 'Q', 'V', 'D', 'F', 'J'], 5: ['T', 'B', 'L', 'S', 'M', 'F', 'N'],
              6: ['P', 'D', 'C', 'H', 'V', 'N', 'R'],
              7: ['T', 'C', 'H'], 8: ['P', 'H', 'N', 'Z', 'V', 'J', 'S', 'G'], 9: ['G', 'H', 'F', 'Z']}


def day5_part1(dictionary):
    for line in lines:
        _m, nr_moves, _f, nr_from, _t, nr_to = line.split()

        for move in range(int(nr_moves)):
            crate = dictionary[int(nr_from)].pop(0)
            dictionary[int(nr_to)].insert(0, crate)

    result = ''
    for position in dictionary:
        top_crate = dictionary[position][0]
        result += top_crate

    return result


def day5_part2(dictionary):
    for line in lines:
        _m, nr_moves, _f, nr_from, _t, nr_to = line.split()


        # crates picked up
        pickUp = dictionary[int(nr_from)][0:int(nr_moves)]

        # remove the crates from list
        dictionary[int(nr_from)] = dictionary[int(nr_from)][int(nr_moves):len(dictionary[int(nr_from)])]

        # add crates to next list
        pickUp.extend(dictionary[int(nr_to)])
        dictionary[int(nr_to)] = pickUp


    result = ''
    for position in dictionary:
        top_crate = dictionary[position][0]
        result += top_crate
    return result

