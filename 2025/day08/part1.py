import os
from math import sqrt

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

for distance in distances[:1001]:
    min_boxes = [boxes[distance[0][0]], boxes[distance[0][1]]]

    # Skip but count connecting junction boxes in the same circuit
    if min_boxes[0]["circuit"] == min_boxes[1]["circuit"]:
        continue

    circuit_to_remove = min_boxes[1]["circuit"]

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

total = 1
max_circuits = []

for i in range(3):
    max_size = 0
    max_circuit = None

    for circuit in circuits:
        if len(circuit) > max_size and circuit not in max_circuits:
            max_size = len(circuit)
            max_circuit = circuit

    max_circuits.append(max_circuit)
    total *= max_size

print(
    f"After connecting 1000 pairs of junction boxes, the size of the top 3 circuits is {total}"
)
