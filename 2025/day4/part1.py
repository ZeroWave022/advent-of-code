import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    lines[i] = list(line)

total = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != "@":
            continue

        adjacent_rolls = 0

        # Top row
        if i >= 1:
            if j - 1 >= 0:
                adjacent_rolls += 1 if lines[i - 1][j - 1] == "@" else 0
            adjacent_rolls += 1 if lines[i - 1][j] == "@" else 0
            if j + 1 < len(line):
                adjacent_rolls += 1 if lines[i - 1][j + 1] == "@" else 0

        # Left and right
        if j > 0:
            adjacent_rolls += 1 if line[j - 1] == "@" else 0
        if j + 1 < len(line):
            adjacent_rolls += 1 if line[j + 1] == "@" else 0

        # Bottom row
        if i + 1 < len(lines):
            if j - 1 >= 0:
                adjacent_rolls += 1 if lines[i + 1][j - 1] == "@" else 0
            adjacent_rolls += 1 if lines[i + 1][j] == "@" else 0
            if j + 1 < len(line):
                adjacent_rolls += 1 if lines[i + 1][j + 1] == "@" else 0

        if adjacent_rolls < 4:
            total += 1

print(f"Total number of accessible paper rolls is {total}")
