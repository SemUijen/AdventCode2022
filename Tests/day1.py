with open('../data/Day1_input.txt') as f:
    lines = f.readlines()


def Puzzle1():
    temp_score = 0
    best_score = 0
    for line in lines:
        if line == '\n':
            if temp_score > best_score:
                best_score = temp_score

            temp_score = 0

        else:
            line = line.replace('\n','')
            temp_score += int(line)

def Puzzle2():
    temp_score = 0
    best_score1 = 0
    best_score2 = 0
    best_score3 = 0
    result_list = []
    for line in lines:
        if len(result_list) > 3:
            result_list.pop(3)
        if line == '\n':
            if result_list == []:
                result_list.append(temp_score)
                temp_score = 0
            else:

                if temp_score > best_score3:
                    if temp_score > best_score2:
                        if temp_score > best_score1:
                            best_score1 = temp_score
                            temp_score = 0

                        else:
                            best_score2 = temp_score
                            temp_score = 0
                    else:
                        best_score3 = temp_score
                        temp_score = 0



                else:
                    temp_score = 0



        else:
            line = line.replace('\n','')
            temp_score += int(line)


    print(sum([best_score1,best_score2,best_score3]))
Puzzle2()
