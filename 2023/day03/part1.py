import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def is_engine_part_number(line: str, starts_at: int, ends_at: int):
    # The lines to check for symbols
    lines_start = lines.index(line) - 1 if lines.index(line) - 1 > 0 else 0
    lines_end = lines.index(line) + 2 if lines.index(line) + 2 < len(lines) else len(lines) - 1

    # Where the symbols indicating a part number can be
    symbols_start_at = starts_at - 1 if starts_at - 1 > 0 else 0
    symbols_end_at = ends_at + 1 if ends_at + 1 < len(line) else len(line)

    # current_line = lines.index(line)
    rows = [r[symbols_start_at:symbols_end_at] for r in lines[lines_start:lines_end]]

    for row in rows:
        if len(re.findall(r"[^.0-9]", row)) >= 1:
            return True

    return False


part_nums = []

for line in lines:
    numbers = re.finditer(r"\d+", line)

    for number in numbers:
        start = number.start()
        end = number.end()
        if is_engine_part_number(line, start, end):
            part_nums.append(int(number.string[start:end]))

print(f"The sum of the part numbers is: {sum(part_nums)}")
