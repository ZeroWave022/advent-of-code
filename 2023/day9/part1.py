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
        last_below = rows[i][-1]

        if last_below == 0:
            rows[i].append(0)

        rows[i-1].append(rows[i-1][-1] + last_below)

    next_values.append(rows[0][-1])

print(sum(next_values))
