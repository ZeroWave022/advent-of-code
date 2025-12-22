import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

for line_num, line in enumerate(lines[1:], 1):
    round_stones = re.finditer("O", line)
    for stone in round_stones:
        pos = stone.start()
        i = line_num
        while lines[i-1][pos] == ".":
            lines[i] = lines[i][:pos] + "." + lines[i][pos+1:]
            lines[i-1] = lines[i-1][:pos] + "O" + lines[i-1][pos+1:]
            if i > 1:
                i -= 1

total_load = 0

for i, line in enumerate(lines):
    stones_on_line = line.count("O")
    total_load += stones_on_line * (len(lines)-i)

print(f"The total load on the north support beams is: {total_load}")
