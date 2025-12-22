import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

times = re.findall(r"\d+", lines[0])
time = int("".join(times))

distances = re.findall(r"\d+", lines[1])
distance = int("".join(distances))

ways_to_win = 0

for i in range(1, time):
    dist = (time - i) * i

    if dist > distance:
        ways_to_win += 1

print(ways_to_win)
