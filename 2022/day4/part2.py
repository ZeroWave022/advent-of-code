import os

path = os.path.join(".", "day_4_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

raw_pairs = [pairs.split(",") for pairs in raw_data]

pairs: list[list[list[str]]] = list()

for pair in raw_pairs:
    processed_pair = [all_floors.split("-") for all_floors in pair]
    pairs.append(processed_pair)

count = 0

for pair in pairs:
    # Convert the pairs to integers
    pair_0 = [int(i) for i in pair[0]]
    pair_1 = [int(i) for i in pair[1]]

    # Create ranges for each pair
    range_1 = range(pair_0[0], pair_0[1] + 1)
    range_2 = range(pair_1[0], pair_1[1] + 1)

    # Check if any pair (partially) includes the other
    if pair_0[0] in range_2 or pair_0[1] in range_2:
        count += 1
    elif pair_1[0] in range_1 or pair_1[1] in range_1:
        count += 1

print(count)
