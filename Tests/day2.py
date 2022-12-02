lines =  open('../data/Day2_data.txt', 'r')

dictionary = {"A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2}

Choice_score = [1,2,3]

def day2_part1():
    result_score_M = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]
    score = 0
    for line in lines:

        score += result_score_M[dictionary[line[0]]][dictionary[line[2]]] + Choice_score[dictionary[line[2]]]

    return score

def day2_part2():
    result_matchfix_score = [0, 3, 6]
    choice_M = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]
    score = 0
    for line in lines:

        score += result_matchfix_score[dictionary[line[2]]] + choice_M[dictionary[line[0]]][dictionary[line[2]]]

    return score

print(day2_part2())