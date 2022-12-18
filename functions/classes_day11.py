import operator
import math
from decimal import Decimal
import sys
from decimal import Context

class KeepAwayGroup:
    def __init__(self):
        self.Monkeys = []

    def find_monkey(self, id):

        if self.Monkeys:
            for monkey in self.Monkeys:
                if id == monkey.id:
                    return monkey

        else:
            return "No Monkeys"

    def print_monkey_items(self):
        if self.Monkeys:
            for monkey in self.Monkeys:
                print(monkey.items)

        else:
            return "No Monkeys"

    def two_best_monkeys(self):
        highest_scores = []
        if self.Monkeys:
            for monkey in self.Monkeys:
                print(monkey.number_inspected)
                highest_scores.append(monkey.number_inspected)

            highest_scores.sort(reverse=True)
            return highest_scores[0] * highest_scores[1]

        else:
            return "No Monkeys"


class Monkey:
    def __init__(self, id):
        self.id = id

        self.items = []

        self.inspection_operator = ""
        self.operation_value = 0

        self.test_value = 0
        self.monkey_true = 0
        self.monkey_false = 0

        self.number_inspected = 0

    def inspect_operation(self, item):
        if self.operation_value == 'old':
            val = item
            ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

            return math.floor((ops[self.inspection_operator](item, val)) / 3)
        else:
            val = int(self.operation_value)
            ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

            return math.floor((ops[self.inspection_operator](item, val)) / 3)

    def throw_test(self, item):
        if item % self.test_value == 0:
            return self.monkey_true
        else:
            return self.monkey_false

    def to_string(self):
        string = ("ID: " + str(self.id),
                  "Operation: " + str(self.inspection_operator) + str(self.operation_value),
                  "Test: " + str(self.test_value),
                  "Monkey True: " + str(self.monkey_true),
                  "Monkey False: " + str(self.monkey_false))

        return print(str(string))

    def inspect_operation_2(self, item):
        if self.operation_value == 'old':
            val = item
            ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
            return ops[self.inspection_operator](item, val)

        else:
            val = int(self.operation_value)
            ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

            return ops[self.inspection_operator](item, val)
