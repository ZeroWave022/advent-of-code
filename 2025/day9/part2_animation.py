"""This is an animated version of the solution for day 9, part 2"""

import os
from time import sleep
from rich.text import Text
from rich.console import Console


def show_matrix(
    matrix: list[list],
    red: list[list],
    green: list[list],
    yellow: list[list],
    info=None,
    blue: list[list] | None = None,
):
    console.clear()
    console.print(title)
    if info:
        console.print(info)

    text = Text()

    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            char = str(char)
            if (i, j) in yellow:
                text.append(char, style="bold yellow")
                continue
            if blue and (i, j) in blue:
                text.append(char, style="bold blue1")
                continue
            if (i, j) in red:
                text.append(char, style="red")
                continue
            if (i, j) in green:
                text.append(char, style="green")
                continue
            text.append(char)
        text.append("\n")

    console.print(text)


path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

points = [[int(i), int(j)] for i, j in [line.split(",") for line in lines]]

# The x and y coordinates must be sorted to
# use coordinate compression below
x_points = list(sorted(list(set(int(p[0]) for p in points))))
y_points = list(sorted(list(set(int(p[1]) for p in points))))

# Coordinate compression
# These dictionaries will map "real" coordinates
# to "minified" versions.
# E.g. 10 -> 1, 12 -> 2, 20 -> 3, 1000 -> 4, etc.
# This decreases the size of the matrix.
x_vals = {}
y_vals = {}

for x in x_points:
    x_vals[x] = len(x_vals)

for y in y_points:
    y_vals[y] = len(y_vals)

console = Console()
title = Text("Advent of Code 2025 - Day 9 (Part 2)", style="bold gold3")

console.clear()
console.print(title)
print("Usually, coordinate compression would be done to decrease matrix size...\n")
console.print("x       | y")

for x, y in zip(x_points[:25], y_points[:25]):
    x_part = f"{x} -> {x_vals[x]}"
    if len(x_part) < 7:
        x_part += " " * (7 - len(x_part))

    console.print(f"{x_part} | {y} -> {y_vals[y]}")
print("Etc...\n")
console.print("For the purpose of the animation, this won't be done", style="bold red")

# Use the coordinates without compression
# for the animation
for x in x_points:
    x_vals[x] = x

for y in y_points:
    y_vals[y] = y

sleep(10)

# Adjusted for non-compressed coordinates
point_map = [[0] * (max(y_vals.values()) + 1) for _ in range(max(x_vals.values()) + 1)]
red = []
green = []
yellow = []
info = Text("Drawing lines between red tiles...\n", style="bold")

show_matrix(point_map, red, green, yellow, info)
sleep(3)

# Draw lines between red tiles
for i, point_1 in enumerate(points):
    x1, y1 = x_vals[point_1[0]], y_vals[point_1[1]]
    red.append((x1, y1))
    for point_2 in points[i + 1 :]:
        x2, y2 = x_vals[point_2[0]], y_vals[point_2[1]]
        if x1 == x2:
            start, end = min(y1, y2), max(y1, y2)
            for k in range(start, end + 1):
                point_map[x1][k] = 1
                green.append((x1, k))
        if y1 == y2:
            start, end = min(x1, x2), max(x1, x2)
            for k in range(start, end + 1):
                point_map[k][y1] = 1
                green.append((k, y1))
        if x1 == x2 or y1 == y2:
            show_matrix(point_map, red, green, yellow, info)
            sleep(0.75)

fill_start = None

info = Text(
    "Trying to find the first upper left corner of the polygon...\n", style="bold"
)

show_matrix(point_map, red, green, yellow, info)
sleep(5)

# Find the first upper left corner
# The "0" closest to this corner must be inside the polygon
for i, row in enumerate(point_map[1:], 1):
    for j, num in enumerate(row):
        show_matrix(point_map, red, green, [(i, j)], info)
        sleep(0.25)
        if num == 1:
            continue

        if (
            row[j - 1] == 1
            and point_map[i - 1][j - 1] == 1
            and point_map[i - 1][j] == 1
        ):
            fill_start = (i, j)
            break

    if fill_start:
        break


info = Text("Found an upper left corner!\n", style="bold green")

show_matrix(point_map, red, green, [fill_start], info)
sleep(3)

info = Text(
    "Filling the polygon using a variant of the flood fill algorithm...\n", style="bold"
)

show_matrix(point_map, red, green, yellow, info)
sleep(5)

fill_queue = [fill_start]

# Fill all tiles inside the polygon
# by using the first starting tile that's inside
# the polygon, and then filling it's neighbors
# until we hit the edges
while len(fill_queue) != 0:
    node = fill_queue.pop()
    point_map[node[0]][node[1]] = 1
    green.append(node)

    if node[0] - 1 > 0 and point_map[node[0] - 1][node[1]] != 1:
        fill_queue.append((node[0] - 1, node[1]))

    if node[0] + 1 < len(point_map) and point_map[node[0] + 1][node[1]] != 1:
        fill_queue.append((node[0] + 1, node[1]))

    if node[1] - 1 > 0 and point_map[node[0]][node[1] - 1] != 1:
        fill_queue.append((node[0], node[1] - 1))

    if node[1] + 1 < len(point_map[0]) and point_map[node[0]][node[1] + 1] != 1:
        fill_queue.append((node[0], node[1] + 1))

    show_matrix(point_map, red, green, fill_queue, info)
    sleep(0.5)

max_area = 0

info = Text("Done filling the polygon!\n", style="bold")

show_matrix(point_map, red, green, yellow, info)
sleep(5)


info = Text("Checking all combinations of rectangles...\n", style="bold")
info.append("Correct rectangles are ")
info.append("blue\n", style="bold blue1")
info.append("Incorrect rectangles are ")
info.append("yellow\n", style="bold yellow")

show_matrix(point_map, red, green, yellow, info)
sleep(10)

for i, corner_1 in enumerate(points):
    x1, y1 = x_vals[corner_1[0]], y_vals[corner_1[1]]
    for corner_2 in points[i + 1 :]:
        x2, y2 = x_vals[corner_2[0]], y_vals[corner_2[1]]

        min_x, max_x = (x1, x2) if x1 <= x2 else (x2, x1)
        min_y, max_y = (y1, y2) if y1 <= y2 else (y2, y1)

        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                yellow.append((i, j))

        # If there's any zeroes in our rectangle, it's outside the polygon
        if any(0 in row[min_y : max_y + 1] for row in point_map[min_x : max_x + 1]):
            show_matrix(point_map, red, green, yellow, info)
            sleep(1)
            yellow = []
            continue

        area = (abs(corner_1[0] - corner_2[0]) + 1) * (
            abs(corner_1[1] - corner_2[1]) + 1
        )

        blue = yellow.copy()
        yellow = []

        found_info = info.copy()
        found_info.append(
            f"\nFound a new valid rectangle!\nArea: {area}", style="bold green"
        )

        show_matrix(point_map, red, green, yellow, found_info, blue)
        sleep(1)

        max_area = max(max_area, area)

console.print(
    f"The biggest rectangle has an area of {max_area}",
    style="bold gold3",
    highlight=False,
)
