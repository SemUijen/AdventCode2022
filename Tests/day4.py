lines = open('../data/day4_input.txt', 'r')


def day4_part1():
    score = 0
    for line in lines:

        elf1 = line.split(sep=',')[0]
        elf2 = line.split(sep=',')[1].replace('\n', '')
        if int(elf1.split(sep='-')[0]) <= int(elf2.split(sep='-')[0]) and int(elf1.split(sep='-')[1]) >= int(
                elf2.split(sep='-')[1]):
            score += 1

        else:
            if int(elf1.split(sep='-')[0]) >= int(elf2.split(sep='-')[0]) and int(elf1.split(sep='-')[1]) <= int(
                    elf2.split(sep='-')[1]):
                score += 1

    return score


def day4_part1_option2():
    score = 0
    for line in lines:
        elf1 = line.split(sep=',')[0]
        elf2 = line.split(sep=',')[1].replace('\n', '')

        elf1_list = list(range(int(elf1.split(sep='-')[0]), int(elf1.split(sep='-')[1])+1))
        elf2_list = list(range(int(elf2.split(sep='-')[0]), int(elf2.split(sep='-')[1])+1))

        for i in elf1_list:
            if i in elf2_list:
                score += 1
                break

    return score


print(day4_part1_option2())
