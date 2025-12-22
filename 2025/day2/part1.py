import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    line = f.read()

ranges = line.split(",")
invalid_total = 0

for id_range in ranges:
    start, end = id_range.split("-")
    for i in range(int(start), int(end) + 1):
        current_id = str(i)
        length = len(current_id)
        if length % 2 != 0:
            continue

        if current_id[: length // 2] == current_id[length // 2 :]:
            invalid_total += i

print(f"Sum of invalid IDs is {invalid_total}")
