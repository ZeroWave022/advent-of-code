import os
from typing import Literal

path = os.path.join(os.path.dirname(__file__), "day_8_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

def calc_view_distance(height_self: int, other_heights: list[int], direction: Literal["left", "right", "up", "down"]) -> int:
    view_distance = 0
    # For left and top, the list needs to be reversed to find the correct view distance.
    if direction in ["left", "up"]:
        other_heights = list(reversed(other_heights))

    for height in other_heights:
        view_distance += 1
        if height >= height_self:
            break

    return view_distance

def calc_scenic_score(column: int, row: int, height_self: int) -> int:
    """Takes a column and row (both zero-indexed), and height of the tree at that location.
    Returns an int indicating its scenic score."""
    # All trees in the grid border will have at least one viewing distance equal to 0.
    if column == 0 or column == len(tree_lines[0]):
        return 0

    heights_left = tree_lines[row][0:column]
    heights_right = tree_lines[row][column+1:]
    heights_over = []
    heights_under = []

    for index, tree_line in enumerate(tree_lines):
        if index < row:
            heights_over.append(tree_line[column])
        elif index > row:
            heights_under.append(tree_line[column])

    # vd: view distance
    left_vd = calc_view_distance(height_self, heights_left, "left")
    right_vd = calc_view_distance(height_self, heights_right, "right")
    up_vd = calc_view_distance(height_self, heights_over, "up")
    down_vd = calc_view_distance(height_self, heights_under, "down")

    return left_vd * right_vd * up_vd * down_vd

tree_lines: list[list[int]] = []

for line in raw_data:
    tree_line = list(line)
    tree_lines.append([int(num) for num in tree_line])

max_score = 0

# Loop through rows, excluding top and bottom
for row, line in enumerate(tree_lines[1:-1]):
    for column, height in enumerate(line):
        new_score = calc_scenic_score(column, row+1, height)
        if new_score > max_score:
            max_score = new_score

print(f"The maximum scenic score is: {max_score}")
