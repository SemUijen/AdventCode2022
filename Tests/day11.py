from functions.classes_day11 import KeepAwayGroup, Monkey
from tqdm import tqdm

lines = open('../data/Day11_input.txt', 'r')


def Setup_keepaway_group():
    keepaway_group = KeepAwayGroup()
    for line in lines:
        split = line.split()

        if 'Monkey' in split:
            monkey_id = int(split[1][0])
            keepaway_group.Monkeys.append(Monkey(monkey_id))
        if 'Starting' in split:
            items = line.split(':')
            items = items[1].replace('\n', '').split(',')
            map1 = map(int, items)
            keepaway_group.find_monkey(monkey_id).items.extend(list(map1))

        if "Operation:" in split:
            keepaway_group.find_monkey(monkey_id).inspection_operator = split[4]
            keepaway_group.find_monkey(monkey_id).operation_value = split[-1]
        if "Test:" in split:
            keepaway_group.find_monkey(monkey_id).test_value = int(split[-1])

        if 'true:' in split:
            keepaway_group.find_monkey(monkey_id).monkey_true = int(split[-1])

        if 'false:' in split:
            keepaway_group.find_monkey(monkey_id).monkey_false = int(split[-1])

    return keepaway_group


def day11_part1():
    keepaway_group = Setup_keepaway_group()
    for _1 in range(20):

        for monkey in keepaway_group.Monkeys:
            for _ in range(len(monkey.items)):
                item = monkey.items.pop()

                item = monkey.inspect_operation(item)
                new_monkey = monkey.throw_test(item)
                keepaway_group.find_monkey(new_monkey).items.append(item)
                monkey.number_inspected += 1

    return keepaway_group.two_best_monkeys()


def day11_part2():
    keepaway_group = Setup_keepaway_group()
    mod = 1
    for monkey in keepaway_group.Monkeys:
        mod *= monkey.test_value
    for _r in tqdm(range(10000)):

        for monkey in keepaway_group.Monkeys:
            for _m in range(len(monkey.items)):
                item = monkey.items.pop()
                item %= mod
                item = monkey.inspect_operation_2(item)
                new_monkey = monkey.throw_test(item)
                keepaway_group.find_monkey(new_monkey).items.append(item)
                monkey.number_inspected += 1

    #keepaway_group.print_monkey_items()
    return keepaway_group.two_best_monkeys()


print(day11_part2())
