import os
import string

path = os.path.join(".", "day_3_input.txt")

with open(path, encoding="utf-8") as f:
    raw_rucksacks = f.read().splitlines()

rucksacks: list[list[str]] = []

for rucksack in raw_rucksacks:
    divider = int(len(rucksack)/2)
    rucksacks.append([rucksack[:divider], rucksack[divider:]])

duplicate_items: list[str] = []

for rucksack in rucksacks:
    for item in rucksack[0]:
        if item in rucksack[1]:
            duplicate_items.append(item)
            break

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

total = 0

for item in duplicate_items:
    if item.islower():
        priority = lowercase.index(item) + 1
    else:
        priority = uppercase.index(item) + 27

    total += priority

print(total)
