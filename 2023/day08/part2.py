import os
import math

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

directions = lines[0]
locations = {}

for line in lines[2:]:
    locations[line[:3]] = tuple(line[7:-1].split(", "))

def calculate_steps(start):
    current_loc = start
    moves = 0
    found = False
    while not found:
        for move in directions:
            if move == "L":
                current_loc = locations[current_loc][0]
            else:
                current_loc = locations[current_loc][1]

            moves += 1

            if current_loc.endswith("Z"):
                found = True
                break

    return moves

start_locs = [loc for loc in locations if loc.endswith("A")]
all_moves = []
for loc in start_locs:
    all_moves.append(calculate_steps(loc))

# The input is generated in a way that makes it possible to use
# the LCM of all path lenghts to find when all of them
# will reach a location ending with Z.
# Each ghost has one **Z location, and all cycles are synchronized
# in a way enabling this.
print(f"All ghosts will arrive after {math.lcm(*all_moves)} steps.")
