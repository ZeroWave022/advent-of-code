import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n\n")

def find_horizontal_reflection(pattern):
    for index in range(0, len(pattern)-1):
        found = True
        for i in range(index+1):
            if index + i + 1 > len(pattern) - 1:
                continue

            if pattern[index-i] != pattern[index+i+1]:
                found = False
                break

        if found:
            return index + 1

def find_vertical_reflection(pattern):
    converted = []
    for i in range(len(pattern[0])):
        converted.append("".join([l[i] for l in pattern]))

    return find_horizontal_reflection(converted)


patterns = []

for pattern in lines:
    patterns.append(pattern.split("\n"))

total = 0

for pattern in patterns:
    vertical = find_vertical_reflection(pattern)
    if vertical:
        total += vertical
    else:
        total += find_horizontal_reflection(pattern) * 100

print(f"The sum of reflection values is: {total}")
