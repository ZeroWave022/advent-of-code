import os

path = os.path.join(os.path.dirname(__file__), "day_6_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read()

for index, char in enumerate(raw_data[2:]):
    # Index is lower by 3 compared to the original data, since enumerate started at original index 2.
    # Therefore the last four characters are accessed with [index:index+4]
    if len(set(raw_data[index:index+4])) == 4:
        # Index is lower than expected, so adjust for original data length
        print(f"Found four unique characters at position {index+4}")
        break
