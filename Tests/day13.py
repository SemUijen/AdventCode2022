lines = open('../data/Day13_test.txt', 'r')
pair_list = lines.read().strip().split("\n\n")
clean_list = list(map(str.splitlines, pair_list))
print(clean_list)

def day13_part1(x, y):
    score = 0

    for a, b in zip(x, y):

        print('a: ', a, b)
        if type(a) == int and type(b) == int:
            if a < b:
                print('score')
                return 1
            if a > b:
                return 0

        if type(a) == list and type(b) == list:
           score = day13_part1(a, b)

        if type(a) == list and type(b) == int:
            temp_list = []
            temp_list.append(b)
            score = day13_part1(a, temp_list)

        if type(a) == int and type(b) == list:
            temp_list = []
            temp_list.append(a)
            score = day13_part1(temp_list, b)

    if score == 2:
        print(len(x))
        return 1

    return 1
score = 0
for x, y in clean_list:
    score += day13_part1(eval(x), eval(y))

print('score: ', score)
