import os
import re

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

rows = []

# Read the digits from each line,
# not taking placement into account
for line in lines[:-1]:
    digits = re.findall(r"\d+", line)
    rows.append(digits)

column_lens = []

for i in range(len(rows[0])):
    column_lens.append(max(len(rows[j][i]) for j in range(len(rows))))

problems = []

# Read each line, column by column,
# based on the calculated column length
# to capture the offset for each number
for line in lines[:-1]:
    digits = []
    col = 0
    for col_length in column_lens:
        digits.append(line[col : col + col_length])
        col += col_length + 1
    problems.append(digits)

operations = re.findall(r"\*|\+", lines[-1])
total = 0

for i, operation in enumerate(operations):
    res = 0 if operation == "+" else 1

    digits = max(len(row[i]) for row in problems)
    for d in range(digits):
        num = ""
        for row in problems:
            if row[i][d] == " ":
                continue
            num += row[i][d]

        res = res + int(num) if operation == "+" else res * int(num)
    total += res


print(f"The sum of the answers is {total}")
