input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

cycle = 17 * 7 * 13 * 2 * 19 * 3 * 5 * 11

class Monkey:
    def __init__(self, items, op_type, op_value, div_test):
        self.items = items
        self.op_type = op_type
        self.op_value = op_value
        self.div_test = div_test
        self.toss_to_true = None
        self.toss_to_false = None
        self.inspections = 0

    def set_targets(self, toss_to_true, toss_to_false):
        self.toss_to_true = toss_to_true
        self.toss_to_false = toss_to_false

    def _run_operation(self, value):
        if self.op_type == "mul":
            return value * self.op_value

        if self.op_type == "sqr":
            return value * value

        # sum
        return value + self.op_value

    def catch_item(self, item):
        self.items.append(item % cycle)

    def run_round(self):
        for item in self.items:
            self.inspections += 1

            worry_value = self._run_operation(value=item)
            # bored_value = worry_value // 3

            if worry_value % self.div_test == 0:
                self.toss_to_true.catch_item(worry_value)
            else:
                self.toss_to_false.catch_item(worry_value)

        self.items = []


# Setup playground
# monkeys = [
#     Monkey([79, 98], "mul", 19, 23),  # 2, 3
#     Monkey([54, 65, 75, 74], "sum", 6, 19),  # 2, 0
#     Monkey([79, 60, 97], "sqr", 0, 13),  # 1, 3
#     Monkey([74], "sum", 3, 17),  # 0, 1
# ]
#
# monkeys[0].set_targets(toss_to_true=monkeys[2], toss_to_false=monkeys[3])
# monkeys[1].set_targets(toss_to_true=monkeys[2], toss_to_false=monkeys[0])
# monkeys[2].set_targets(toss_to_true=monkeys[1], toss_to_false=monkeys[3])
# monkeys[3].set_targets(toss_to_true=monkeys[0], toss_to_false=monkeys[1])

# Setup playground
monkeys = [
    Monkey([89, 74], "mul", 5, 17),
    Monkey([75, 69, 87, 57, 84, 90, 66, 50], "sum", 3, 7),
    Monkey([55], "sum", 7, 13),
    Monkey([69, 82, 69, 56, 68], "sum", 5, 2),
    Monkey([72, 97, 50], "sum", 2, 19),
    Monkey([90, 84, 56, 92, 91, 91], "mul", 19, 3),
    Monkey([63, 93, 55, 53], "sqr", 0, 5),
    Monkey([50, 61, 52, 58, 86, 68, 97], "sum", 4, 11),
]

monkeys[0].set_targets(toss_to_true=monkeys[4], toss_to_false=monkeys[7])
monkeys[1].set_targets(toss_to_true=monkeys[3], toss_to_false=monkeys[2])
monkeys[2].set_targets(toss_to_true=monkeys[0], toss_to_false=monkeys[7])
monkeys[3].set_targets(toss_to_true=monkeys[0], toss_to_false=monkeys[2])
monkeys[4].set_targets(toss_to_true=monkeys[6], toss_to_false=monkeys[5])
monkeys[5].set_targets(toss_to_true=monkeys[6], toss_to_false=monkeys[1])
monkeys[6].set_targets(toss_to_true=monkeys[3], toss_to_false=monkeys[1])
monkeys[7].set_targets(toss_to_true=monkeys[5], toss_to_false=monkeys[4])

number_of_rounds = 10000

for i in range(0, number_of_rounds):
    for monkey in monkeys:
        monkey.run_round()

inspections = [monkey.inspections for monkey in monkeys]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
