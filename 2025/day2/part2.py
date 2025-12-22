import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    line = f.read()


def has_repeating_pattern(string: str, pattern_length: int):
    pattern = string[:pattern_length]
    for i in range(pattern_length, len(string), pattern_length):
        if pattern != string[i : i + pattern_length]:
            return False
    return True


ranges = line.split(",")
invalid_total = 0

for id_range in ranges:
    start, end = id_range.split("-")
    for i in range(int(start), int(end) + 1):
        current_id = str(i)
        for j in range(1, len(current_id)):
            if has_repeating_pattern(current_id, j):
                invalid_total += i
                break

print(f"Sum of invalid IDs is {invalid_total}")
