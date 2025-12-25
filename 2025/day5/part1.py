import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

raw_ranges = []
total = 0

while True:
    if lines[0] == "":
        lines.pop(0)
        break
    raw_ranges.append(lines[0])
    lines.pop(0)

ranges = []

# Instead of comparing insanely big ranges (15 digit numbers)
# Let's save the "offset" to the start, and how big the range is ("end")
for r in raw_ranges:
    start, stop = r.split("-")
    start, stop = int(start), int(stop)
    stop -= start
    ranges.append({"offset": start, "end": stop})

# For each food ID, subtract the offset
# and check if we're in the range
for food_id in lines:
    food_id = int(food_id)
    for r in ranges:
        check = food_id - r["offset"]
        if 0 <= check <= r["end"]:
            total += 1
            break

print(f"Total number of fresh ingredients is {total}")
