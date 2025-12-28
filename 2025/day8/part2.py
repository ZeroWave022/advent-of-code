import os
from math import sqrt, inf

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

boxes = []

for line in lines:
    boxes.append([int(digit) for digit in line.split(",")])

boxes = [{"pos": box, "circuit": i} for i, box in enumerate(boxes)]
circuits = [[box] for box in boxes]

distances = {}

for i, box_1 in enumerate(boxes):
    for j, box_2 in enumerate(boxes[i + 1 :], i + 1):
        distances[i, j] = sqrt(
            (box_1["pos"][0] - box_2["pos"][0]) ** 2
            + (box_1["pos"][1] - box_2["pos"][1]) ** 2
            + (box_1["pos"][2] - box_2["pos"][2]) ** 2
        )

distances = list(sorted(distances.items(), key=lambda k: k[1]))

for distance in distances:
    min_boxes = [boxes[distance[0][0]], boxes[distance[0][1]]]

    circuit_to_remove = min_boxes[1]["circuit"]

    # Skip but count connecting junction boxes in the same circuit
    if min_boxes[0]["circuit"] == min_boxes[1]["circuit"]:
        continue

    # Join the circuits together
    # and remove one of them
    for box in circuits[circuit_to_remove]:
        circuits[min_boxes[0]["circuit"]].append(box)
        box["circuit"] = min_boxes[0]["circuit"]

    circuits.pop(circuit_to_remove)

    # Any indexes that have been offset
    # because of the deletion must be fixed
    for box in boxes:
        if box["circuit"] > circuit_to_remove:
            box["circuit"] -= 1

    if len(circuits) == 2:
        break

min_distance = inf

for box_1 in circuits[0]:
    for box_2 in circuits[1]:
        indexes = boxes.index(box_1), boxes.index(box_2)
        distance = sqrt(
            (box_1["pos"][0] - box_2["pos"][0]) ** 2
            + (box_1["pos"][1] - box_2["pos"][1]) ** 2
            + (box_1["pos"][2] - box_2["pos"][2]) ** 2
        )
        if distance < min_distance:
            min_distance = distance
            min_boxes = [box_1, box_2]

print(
    f"The X coordinate of the last two junction boxes multiplied is {min_boxes[0]["pos"][0] * min_boxes[1]["pos"][0]}"
)
