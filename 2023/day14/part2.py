import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def move_vertically(lines, direction):
    if direction not in ["north", "south"]:
        raise ValueError(f"Unknown vertical direction: {direction}")

    cols = list(map("".join, zip(*lines)))

    for index, col in enumerate(cols):
        parts = col.split("#")
        for i, part in enumerate(parts):
            stones = part.count("O")

            if direction == "north":
                parts[i] = "O" * stones + "." * (len(part)-stones)
            else:
                parts[i] = "." * (len(part)-stones) + "O" * stones

        cols[index] = "#".join(parts)

    return list(map("".join, zip(*cols)))

def move_horizontally(lines, direction):
    if direction not in ["west", "east"]:
        raise ValueError(f"Unknown horizontal direction: {direction}")

    for index, line in enumerate(lines):
        parts = line.split("#")
        for i, part in enumerate(parts):
            stones = part.count("O")
            if direction == "west":
                parts[i] = "O" * stones + "." * (len(part)-stones)
            else:
                parts[i] = "." * (len(part)-stones) + "O" * stones

        lines[index] = "#".join(parts)

    return lines

platforms = []
cycle_length = None
cycle_start = None

for i in range(1_000_000_000):
    lines = move_vertically(lines, "north")
    lines = move_horizontally(lines, "west")
    lines = move_vertically(lines, "south")
    lines = move_horizontally(lines, "east")

    if lines in platforms:
        cycle_start = platforms.index(lines)
        cycle_length = len(platforms) - cycle_start
        break

    platforms.append(lines.copy())

cycles_left = (1_000_000_000 - cycle_start) % cycle_length
final = platforms[cycle_start+cycles_left-1]

total_load = 0

for i, line in enumerate(final):
    stones_on_line = line.count("O")
    total_load += stones_on_line * (len(lines)-i)

print(f"After 1 000 000 000 cycles, the total load would be: {total_load}")
