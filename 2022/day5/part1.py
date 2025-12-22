import os
import string
import math
import re

path = os.path.join(".", "day_5_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

uppercase = [*string.ascii_uppercase]

crates: dict[str, list] = {}

for line in raw_data:
    if "[" not in line:
        break

    splitted = line.split("[")

    index = splitted[0].count(" ") // 3 + 1

    for part in splitted:
        if len(part) == 0:
            continue

        crate_id = part[0]
        # Divide amount of spaces by 4, always round down and add 1
        distance_next = math.floor(part.count(" ") / 4) + 1

        if not crates.get(str(index)):
            crates[str(index)] = [crate_id]
        else:
            crates[str(index)].append(crate_id)

        index += distance_next

moves: list[dict[str, str]] = []

for line in raw_data:
    if "move" not in line:
        continue

    nums = re.findall(r"\d+", line)

    moves.append({
        "amount": nums[0],
        "from": nums[1],
        "to": nums[2]
    })

for move in moves:
    for i in range(int(move["amount"])):
        from_id = move["from"]
        to_id = move["to"]

        moved_crate = crates[from_id].pop(0)
        crates[to_id].insert(0, moved_crate)

top_crates = []

for i in range(1, len(crates) + 1):
    top_crates.append(crates[str(i)][0])

print("".join(top_crates))
