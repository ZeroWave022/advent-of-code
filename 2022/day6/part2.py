import os

path = os.path.join(os.path.dirname(__file__), "day_6_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read()

for index, char in enumerate(raw_data[13:]):
    # Index is lower by 13 compared to the original data, since enumerate started at original index 13.
    # Therefore the last 14 characters are accessed with [index:index+14]
    if len(set(raw_data[index:index+14])) == 14:
        # Index is lower than expected, so adjust for original data length
        print(f"Found four unique characters at position {index+14}")
        break
