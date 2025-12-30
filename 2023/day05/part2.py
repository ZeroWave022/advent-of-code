import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

conversions = {}

seed_data = [int(seed) for seed in re.findall(r"\d+", lines[0])]
seeds = []

i = 0
while i < len(seed_data):
    start = seed_data[i]
    end = start+seed_data[i+1]
    seeds.append({"start": start, "end": end})
    i += 2

processing = None
for line in lines[1:]:
    if "map" in line:
        processing = line.replace(" map:", "")
        conversions[processing] = []
        continue

    if line == "":
        continue

    nums = [int(num) for num in line.split(" ")]

    conversions[processing].append(nums)

def find_included(range_1, range_2):
    return range(max(range_1.start, range_2.start), min(range_1.stop, range_2.stop)) or None

def convert_to_next(seed, dest, source):
    return seed + dest - source

all_ranges = []

for seed_range in seeds:
    ranges = [range(seed_range["start"], seed_range["end"])]

    for conversion in conversions.values():
        updated = []
        for dest_start, source_start, range_len in conversion:
            for range_index, r in enumerate(ranges):
                if r in updated:
                    continue

                sources = range(source_start, source_start+range_len)
                included = find_included(sources, r)

                if included:
                    start = convert_to_next(included.start, dest_start, source_start)
                    end = convert_to_next(included.stop, dest_start, source_start)
                    ranges[range_index] = range(start, end)

                    updated.append(range(start, end))

                    if included.start > r.start:
                        ranges.append(range(r.start, included.start))

                    if included.stop < r.stop:
                        ranges.append(range(included.stop, r.stop))

    all_ranges.extend(ranges.copy())

print(f"The smallest location is: {min(r.start for r in all_ranges)}")
