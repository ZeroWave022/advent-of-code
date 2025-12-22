import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def expand_rows(lines: list[str]) -> list[str]:
    new_lines = []
    for line in lines:
        if "#" in line:
            new_lines.append(line)
            continue
        
        new_lines.append("." * len(line))
        new_lines.append(line)
    
    return new_lines

def expand_columns(lines: list[str]) -> list[str]:
    dots_to_be_placed = []
    for i in range(len(lines[0])):
        column = [l[i] for l in lines]
        if "#" in column:
            continue

        dots_to_be_placed.append(i)

    new_lines = []

    for line in lines:
        new_line = line
        for i in reversed(dots_to_be_placed):
            new_line = new_line[:i] + "." + new_line[i:]

        new_lines.append(new_line)

    return new_lines

def find_galaxy_positions(lines: list[str]) -> int:
    positions: list[tuple] = []
    row = 0
    for line in lines:
        if not line.count("#") > 0:
            row += 1
            continue
        
        indexes = [i for i, char in enumerate(line) if char == "#"]

        for index in indexes:
            positions.append((row, index))

        row += 1
    
    return positions


lines = expand_rows(lines)
lines = expand_columns(lines)

positions = find_galaxy_positions(lines)

total_distance = 0

for i, pos_1 in enumerate(positions):
    for pos_2 in positions[i+1:]:
        total_distance += abs(pos_2[0] - pos_1[0]) + abs(pos_2[1] - pos_1[1])

print(f"The total distance is {total_distance}")
