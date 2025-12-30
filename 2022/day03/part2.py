import os
import string

path = os.path.join(".", "day_3_input.txt")

with open(path, encoding="utf-8") as f:
    raw_rucksacks = f.read().splitlines()

badges: list[str] = []

for i in range(0, len(raw_rucksacks), 3):
    group = raw_rucksacks[i:i+3]
    rucksack_sets = [set(rucksack) for rucksack in group]

    repeated = set.intersection(*rucksack_sets)

    if len(list(repeated)) > 1:
        raise NotImplementedError("Found multiple 'badges' in a group of rucksacks.")

    badges.append(list(repeated)[0])


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

total = 0

for badge in badges:
    if badge.islower():
        priority = lowercase.index(badge) + 1
    else:
        priority = uppercase.index(badge) + 27

    total += priority

print(total)
