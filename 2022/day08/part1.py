import os

path = os.path.join(os.path.dirname(__file__), "day_8_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

def is_visible(column: int, row: int, height_self: int) -> bool:
    """Takes a column and row (both zero-indexed), and height of the tree at that location.
    Returns a bool indicating whether it is visible from at least one direction (left, right, top or bottom)."""
    if column == 0 or column == len(tree_lines[0]):
        return True

    heights_left = tree_lines[row][0:column]
    heights_right = tree_lines[row][column+1:]

    # If all the trees to the left or right are smaller than us, we're visible
    if all(h < height_self for h in heights_left) or all(h < height_self for h in heights_right):
        return True

    heights_over = []
    heights_under = []

    for index, line in enumerate(tree_lines):
        if index < row:
            heights_over.append(line[column])
        elif index > row:
            heights_under.append(line[column])

    if all(h < height_self for h in heights_over) or all(h < height_self for h in heights_under):
        return True

    return False

tree_lines: list[list[int]] = []

for line in raw_data:
    tree_line = list(line)
    tree_lines.append([int(num) for num in tree_line])

# Add the whole top and bottom rows which are always visible
trees_visible = len(tree_lines[0]) * 2

# Loop through rows, excluding top and bottom
for row, line in enumerate(tree_lines[1:-1]):
    for column, height in enumerate(line):
        if is_visible(column, row+1, height):
            trees_visible += 1

print(f"The number of trees visible in the grid is: {trees_visible}")
