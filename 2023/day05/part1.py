import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

data = {}

seeds = [int(seed) for seed in re.findall(r"\d+", lines[0])]

processing = None
for line in lines[1:]:
    if "map" in line:
        processing = line.replace(" map:", "")
        data[processing] = []
        continue

    if line == "":
        continue

    nums = [int(num) for num in line.split(" ")]

    data[processing].append(nums)

locations = []

for seed in seeds:
    converted_seed = seed
    for conversions in data.values():
        for conversion in conversions:
            range_from = conversion[1]
            range_to = conversion[1]+conversion[2]
            if converted_seed in range(range_from, range_to):
                converted_seed += conversion[0]-conversion[1]
                break

    locations.append(converted_seed)

print(f"The smallest location is: {min(locations)}")
