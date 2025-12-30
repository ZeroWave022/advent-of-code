import os

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


point_map = [[0] * (len(y_vals) + 1) for _ in range(len(x_vals) + 1)]

# Draw lines between red tiles
for i, point_1 in enumerate(points):
    x1, y1 = x_vals[point_1[0]], y_vals[point_1[1]]
    for point_2 in points[i + 1 :]:
        x2, y2 = x_vals[point_2[0]], y_vals[point_2[1]]
        if x1 == x2:
            start, end = min(y1, y2), max(y1, y2)
            for k in range(start, end + 1):
                point_map[x1][k] = 1
        if y1 == y2:
            start, end = min(x1, x2), max(x1, x2)
            for k in range(start, end + 1):
                point_map[k][y1] = 1

fill_start = None

# Find the first upper left corner
# The "0" closest to this corner must be inside the polygon
for i, row in enumerate(point_map[1:], 1):
    for j, num in enumerate(row):
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

fill_queue = [fill_start]

# Fill all tiles inside the polygon
# by using the first starting tile that's inside
# the polygon, and then filling it's neighbors
# until we hit the edges
while len(fill_queue) != 0:
    node = fill_queue.pop()
    point_map[node[0]][node[1]] = 1

    if node[0] - 1 > 0 and point_map[node[0] - 1][node[1]] != 1:
        fill_queue.append((node[0] - 1, node[1]))

    if node[0] + 1 < len(point_map) and point_map[node[0] + 1][node[1]] != 1:
        fill_queue.append((node[0] + 1, node[1]))

    if node[1] - 1 > 0 and point_map[node[0]][node[1] - 1] != 1:
        fill_queue.append((node[0], node[1] - 1))

    if node[1] + 1 < len(point_map[0]) and point_map[node[0]][node[1] + 1] != 1:
        fill_queue.append((node[0], node[1] + 1))

max_area = 0

for i, corner_1 in enumerate(points):
    x1, y1 = x_vals[corner_1[0]], y_vals[corner_1[1]]
    for corner_2 in points[i + 1 :]:
        x2, y2 = x_vals[corner_2[0]], y_vals[corner_2[1]]

        min_x, max_x = (x1, x2) if x1 <= x2 else (x2, x1)
        min_y, max_y = (y1, y2) if y1 <= y2 else (y2, y1)

        # If there's any zeroes in our rectangle, it's outside the polygon
        if any(0 in row[min_y : max_y + 1] for row in point_map[min_x : max_x + 1]):
            continue

        max_area = max(
            max_area,
            (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1),
        )

print(f"The biggest rectangle has an area of {max_area}")
