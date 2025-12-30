import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

points = [[int(i), int(j)] for i, j in [line.split(",") for line in lines]]

max_area = 0

for i, corner_1 in enumerate(points):
    for corner_2 in points[i + 1 :]:
        new_area = (abs(corner_1[0] - corner_2[0]) + 1) * (
            abs(corner_1[1] - corner_2[1]) + 1
        )
        max_area = max(max_area, new_area)

print(f"The biggest rectangle has an area of {max_area}")
