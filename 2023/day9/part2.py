import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

num_hist = []

for line in lines:
    num_hist.append([int(num) for num in line.split(" ")])

next_values = []

for history in num_hist:
    rows = [history]
    diff = rows[0][1] - rows[0][0]
    index = 0
    while not all(num == 0 for num in rows[-1]):
        new_row = []
        for i in range(len(rows[index])-1):
            diff = rows[index][i+1] - rows[index][i]
            new_row.append(diff)

        rows.append(new_row)
        index += 1

    for i in range(len(rows)-1, 0, -1):
        first_below = rows[i][0]

        if first_below == 0:
            rows[i].insert(0, 0)

        rows[i-1].insert(0, rows[i-1][0] - first_below)

    next_values.append(rows[0][0])

print(sum(next_values))
