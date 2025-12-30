import os
import re

path = os.path.join(os.path.dirname(__file__), "day_9_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

rope = [[0, 0] for _ in range(10)]
tail_visited = []
directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

def move_head(pos, move_to):
    move = directions[move_to]
    pos[0] += move[0]
    pos[1] += move[1]
    return pos

def move_back_knot(knot_front, knot_back):
    delta_col = knot_back[0] - knot_front[0]
    delta_row = knot_back[1] - knot_front[1]

    if abs(delta_col) <= 1 and abs(delta_row) <= 1:
        return knot_back

    if knot_front[0] > knot_back[0]:
        knot_back[0] += 1
    elif knot_front[0] < knot_back[0]:
        knot_back[0] -= 1

    if knot_front[1] > knot_back[1]:
        knot_back[1] += 1
    elif knot_front[1] < knot_back[1]:
        knot_back[1] -= 1

    return knot_back

for move_num, move in enumerate(raw_data, 1):
    direction = move[0]
    steps = int(re.findall(r"\d+", move)[0])

    for _ in range(steps):
        rope[0] = move_head(rope[0], direction)
        for knot in range(1, len(rope)):
            knot_in_front = rope[knot-1]
            rope[knot] = move_back_knot(knot_in_front, rope[knot])

        tail_visited.append(tuple(rope[-1]))

unique_pos = []

for pos in tail_visited:
    if pos not in unique_pos:
        unique_pos.append(pos)

print(f"The number of unique positions the tail visits is {len(unique_pos)}")
