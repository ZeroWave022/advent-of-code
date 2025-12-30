import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

position = 50
zeros = 0

for line in lines:
    rotation = line[0]
    distance = int(line[1:])

    position += distance if rotation == "R" else -distance

    # Noticed that instead of repeatedly subtracting
    # or adding, we can just use modulo
    position %= 100

    if position == 0:
        zeros += 1

print(f"The dial pointed at the number 0 {zeros} times.")
