import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

splits = 0

beams = set([lines[0].index("S")])

for line in lines[1:]:
    for i, char in enumerate(line):
        if char != "^":
            continue

        if i in beams:
            if i - 1 >= 0:
                beams.add(i - 1)
            if i + 1 < len(line):
                beams.add(i + 1)
            beams.remove(i)
            splits += 1

print(f"The beam was split {splits} times")
