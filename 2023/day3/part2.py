import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def get_gear_index(line: str, starts_at: int, ends_at: int):
    # The lines to check for symbols
    lines_start = lines.index(line) - 1 if lines.index(line) - 1 > 0 else 0
    lines_end = lines.index(line) + 2 if lines.index(line) + 2 < len(lines) else len(lines) - 1

    # Where the symbols indicating a part number can be
    symbols_start_at = starts_at - 1 if starts_at - 1 > 0 else 0
    symbols_end_at = ends_at + 1 if ends_at + 1 < len(line) else len(line)

    rows = [r[symbols_start_at:symbols_end_at] for r in lines[lines_start:lines_end]]

    for row in rows:
        if "*" in row:
            return (
                symbols_start_at + row.index("*"),
                lines_start + rows.index(row)
            )

    return None

gear_nums = {}
gear_ratios = []

for line in lines:
    numbers = re.finditer(r"\d+", line)

    for number in numbers:
        start = number.start()
        end = number.end()
        gear_index = get_gear_index(line, start, end)

        if gear_index:
            gear = gear_nums.get(gear_index)
            # If there's already one number attached to that gear,
            # calculate and append the gear ratio
            if gear:
                gear_ratios.append(gear * int(number.string[start:end]))
            else:
                gear_nums[gear_index] = int(number.string[start:end])

print(f"The sum of the gear ratios is: {sum(gear_ratios)}")
