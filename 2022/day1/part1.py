import os

path = os.path.join(".", "day_1_input.txt")

with open(path) as f:
    raw_text = f.read()

inventories_raw = raw_text.split("\n\n")

inventories: list[list[int]] = []

for inventory in inventories_raw:
    new_inventory = [int(i) for i in inventory.split("\n")]
    inventories.append(new_inventory)

max_calories = 0

for inv in inventories:
    calories = sum(inv)
    if calories > max_calories:
        max_calories = calories

print(max_calories)
