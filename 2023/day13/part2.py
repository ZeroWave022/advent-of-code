import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n\n")

def sum_diff_chars(text_1, text_2):
    return sum(text_1[i] != text_2[i] for i in range(len(text_1)))

def find_horizontal_reflection(pattern):
    for index in range(0, len(pattern)-1):
        found = True
        smudge_found = False

        for i in range(index+1):
            if index + i + 1 > len(pattern) - 1:
                continue

            diff_chars = sum_diff_chars(pattern[index-i], pattern[index+i+1])

            if diff_chars > 1:
                found = False
                break
            elif diff_chars == 1:
                if smudge_found:
                    found = False
                    break
                smudge_found = True

        if found and smudge_found:
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
