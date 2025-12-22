import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

direcations = lines[0]
locations = {}

for line in lines[2:]:
    locations[line[:3]] = tuple(line[7:-1].split(", "))

current_loc = "AAA"
moves = 0
while current_loc != "ZZZ":
    for move in direcations:
        if move == "L":
            current_loc = locations[current_loc][0]
        else:
            current_loc = locations[current_loc][1]
        moves += 1

        if current_loc == "ZZZ":
            break

print(f"ZZZ is reached after {moves} moves.")
