import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()


def join_ranges(ranges: list[list]):
    for i, range_1 in enumerate(ranges):
        for j, range_2 in enumerate(ranges):
            # The same range cannot be an extension of itself
            if j == i:
                continue

            # If a range is completely included by another one,
            # remove it
            if range_2[0] <= range_1[0] <= range_2[1] and range_1[1] <= range_2[1]:
                ranges.pop(i)
                return join_ranges(ranges)

            # If range 1 is an extension of range 2 to the left,
            # extend range 2 and remove range 1
            if range_1[0] <= range_2[0] and range_2[0] <= range_1[1] <= range_2[1]:
                range_2[0] = range_1[0]
                ranges.pop(i)
                return join_ranges(ranges)

            # If range 1 is an extension of range 2 to the right,
            # extend range 2 and remove range 1
            if range_2[0] <= range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
                range_2[1] = range_1[1]
                ranges.pop(i)
                return join_ranges(ranges)

            # If two ranges are adjacent to each other,
            # join them
            if range_1[1] == range_2[0] - 1:
                ranges[i][1] = ranges[j][1]
                ranges.pop(j)
                return join_ranges(ranges)


ranges = []

for line in lines:
    if line == "":
        break

    start, end = line.split("-")
    ranges.append([int(start), int(end)])

    # Remove duplicates
    join_ranges(ranges)

total = sum(end - start + 1 for start, end in ranges)

print(f"Total number of food IDs considered fresh is {total}")
