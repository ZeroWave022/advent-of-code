import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

times = [int(t) for t in re.findall(r"\d+", lines[0])]
distances = [int(d) for d in re.findall(r"\d+", lines[1])]

ways_to_win = []

for game, time in enumerate(times):
    possible_ways_to_win = []
    for i in range(1, time):
        dist = (time - i) * i

        if dist > distances[game]:
            possible_ways_to_win.append(i)

    ways_to_win.append(len(possible_ways_to_win))

print(ways_to_win[0] * ways_to_win[1] * ways_to_win[2] * ways_to_win[3])
