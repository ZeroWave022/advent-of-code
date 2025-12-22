import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

numbers = []

for line in lines:
    line_num = ""
    for char in line:
        if char.isdigit():
            line_num += char

    numbers.append(int(line_num[0] + line_num[-1]))

print(f"The sum of all calibration values is: {sum(numbers)}")
