import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

position = 50
zeros = 0

for line in lines:
    rotation = line[0]
    distance = int(line[1:])

    position_before = position

    sign_before = position > 0
    position += distance if rotation == "R" else -distance
    sign_after = position > 0

    if position == 0 or position_before != 0 and sign_before != sign_after:
        zeros += 1

    passed_zero = abs(position) // 100

    if passed_zero > 0:
        zeros += passed_zero

    # Noticed that instead of repeatedly subtracting
    # or adding, we can just use modulo
    position %= 100

print(f"The dial pointed at the number 0 {zeros} times.")
