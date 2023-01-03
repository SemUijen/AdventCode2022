
def day13(x, y):

    if type(x) == int and type(y) == int:
        return x-y
    if type(x) == list and type(y) == int:
        return day13(x, [y])
    if type(x) == int and type(y) == list:
        return day13([x], y)

    for a, b in zip(x, y):
        score = day13(a, b)
        if score:
            return score

    return len(x) - len(y)

# part1
lines = open('../data/Day13_input.txt', 'r')
pair_list = lines.read().strip().split("\n\n")
clean_list = list(map(str.splitlines, pair_list))
score =0
for i, (x, y) in enumerate(clean_list):
    if day13(eval(x), eval(y)) <0:
        score += (i+1)
print('score: ', score)

# part2
clean_list_2 = list(map(eval, open('../data/Day13_input.txt', 'r').read().split()))
i2 = 1
i6 = 2
for a in clean_list_2:
    if day13(a, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif day13(a, [[6]]) < 0:
        i6 += 1
print(i2 * i6)
