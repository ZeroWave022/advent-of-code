import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def convert_to_columns(lines: list[str]) -> list[str]:
    all_columns = []
    for i in range(len(lines[0])):
        all_columns.append([l[i] for l in lines])

    return all_columns

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

def find_empty(pos_1, pos_2, lines, columns):
    empty_rows = 0
    empty_cols = 0

    min_index = min(pos_1[0], pos_2[0])
    max_index = max(pos_1[0], pos_2[0])
    for line in lines[min_index:max_index]:
        if line.count("#") == 0:
            empty_rows += 1

    min_index = min(pos_1[1], pos_2[1])
    max_index = max(pos_1[1], pos_2[1])
    for col in columns[min_index:max_index]:
        if not "#" in col:
            empty_cols += 1

    return (empty_rows, empty_cols)

positions = find_galaxy_positions(lines)
columns = convert_to_columns(lines)

total_distance = 0

for i, pos_1 in enumerate(positions):
    for pos_2 in positions[i+1:]:
        empty = find_empty(pos_1, pos_2, lines, columns)

        total_distance += empty[0] * 1_000_000 + abs(pos_2[0] - pos_1[0]) - empty[0]
        total_distance += empty[1] * 1_000_000 + abs(pos_2[1] - pos_1[1]) - empty[1]

print(f"The total distance is {total_distance}")
