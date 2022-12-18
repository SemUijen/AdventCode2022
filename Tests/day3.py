import string

lines = open('../data/Day3_test.txt', 'r')


def setup_score_dict():
    Alphabet = string.ascii_letters
    score = 1
    score_dict = {}
    for letter in Alphabet:
        score_dict[letter] = score
        score += 1

    return score_dict
setup_score_dict()

def day3_part1():
    score = 0
    score_dict = setup_score_dict()
    for line in lines:
        string1, string2 = line[slice(0, len(line) // 2)], line[slice(len(line) // 2, len(line))]

        for letter in string1:
            if letter in string2:
                score += score_dict[letter]

                break
    return score

def day3_part2():
    score = 0
    score_dict = setup_score_dict()
    temp_list = []
    for line in lines:
        temp_list.append(line)
        if len(temp_list) == 3:
            for letter in temp_list[0]:
                if letter in temp_list[1] and letter in temp_list[2]:
                    score += score_dict[letter]
                    temp_list.clear()
                    break
    return score
print(day3_part2())
