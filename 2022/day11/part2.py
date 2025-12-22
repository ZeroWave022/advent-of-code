import os
import re
import operator
import math

path = os.path.join(os.path.dirname(__file__), "day_11_input.txt")

with open(path, encoding="utf-8") as f:
    data_one_line = f.read()
    raw_data = data_one_line.splitlines()

operations = {
    "+": operator.add,
    "*": operator.mul
}

monkeys = []

monkeys_num = data_one_line.count("Monkey")

for i in range(monkeys_num):
    # 7 is the amount of lines between each monkey info
    start_at = i*7
    items = re.findall(r"\d+", raw_data[start_at+1])
    operation = raw_data[start_at+2].split("old ")[-1]
    divisible_by = int(re.findall(r"\d+", raw_data[start_at+3])[0])
    when_true = int(raw_data[start_at+4].split(" ")[-1])
    when_false = int(raw_data[start_at+5].split(" ")[-1])

    monkeys.append({
        "items": [int(item) for item in items],
        "operation": operation,
        "divisible_by": divisible_by,
        "when_true": when_true,
        "when_false": when_false,
        "inspected": 0
    })

# Worry levels are no longer divided by 3.
# There is a least common multiple (lcm) that can be used together with modulo to keep the worry levels as low as possible.
lcm = math.lcm(*[monkey["divisible_by"] for monkey in monkeys])

rounds = 10_000

for r in range(rounds):
    for monkey in monkeys:
        for item in monkey["items"]:
            oper_str, worry_mult = monkey["operation"].split(" ")
            if worry_mult != "old":
                worry = operations[oper_str](item, int(worry_mult))
            else:
                worry = operations[oper_str](item, item)
            worry %= lcm

            if worry % int(monkey["divisible_by"]) == 0:
                throwing_to = monkeys[monkey["when_true"]]
                throwing_to["items"].append(worry)
            else:
                throwing_to = monkeys[monkey["when_false"]]
                throwing_to["items"].append(worry)

            monkey["inspected"] += 1
        monkey["items"] = []

inspections = sorted([monkey["inspected"] for monkey in monkeys], reverse=True)

print(f"The level of monkey business after 20 rounds is: {inspections[0] * inspections[1]}")
