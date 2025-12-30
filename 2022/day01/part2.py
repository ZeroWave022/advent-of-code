import os

path = os.path.join(".", "day_1_input.txt")

with open(path) as f:
    raw_text = f.read()

inventories_raw = raw_text.split("\n\n")

inventories: list[list[int]] = []

for inventory in inventories_raw:
    new_inventory = [int(i) for i in inventory.split("\n")]
    inventories.append(new_inventory)

calories: list[int] = []

for inv in inventories:
    calories.append(sum(inv))

top_3_total = 0

for i in range(3):
    top_3_total += max(calories)

    index = calories.index(max(calories))

    del calories[index]

print(top_3_total)
