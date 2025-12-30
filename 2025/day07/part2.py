import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()


# Recursive solution which ended up having a too long running time:
# def simulate_timeline(lines: list[str], beam: int):
#     timelines = 0
#     split = False
#     for i, line in enumerate(lines):
#         for pos, char in enumerate(line):
#             if char != "^":
#                 continue

#             if pos == beam:
#                 if pos - 1 >= 0:
#                     timelines += simulate_timeline(lines[i + 1 :], pos - 1)
#                     split = True
#                 if pos + 1 < len(line):
#                     timelines += simulate_timeline(lines[i + 1 :], pos + 1)
#                     split = True

#         if split:
#             return timelines

#     return timelines + 1


def simulate_timeline(lines: list[str], beam: int):
    beams = {beam: 1}
    for line in lines:
        for pos, char in enumerate(line):
            if char != "^":
                continue

            if pos in beams:
                if pos - 1 >= 0:
                    if pos - 1 in beams:
                        beams[pos - 1] += beams[pos]
                    else:
                        beams[pos - 1] = beams[pos]
                if pos + 1 < len(line):
                    if pos + 1 in beams:
                        beams[pos + 1] += beams[pos]
                    else:
                        beams[pos + 1] = beams[pos]
                beams.pop(pos)

    return sum(beams.values())


timelines = simulate_timeline(lines[1:], lines[0].index("S"))

print(f"The number of timelines is {timelines}")
