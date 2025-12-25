import os
import re

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

problems = []

for line in lines[:-1]:
    digits = re.findall(r"\d+", line)
    problems.append([int(i) for i in digits])

operations = re.findall(r"\*|\+", lines[-1])
total = 0

for i, operation in enumerate(operations):
    if operation == "+":
        total += sum(problems[j][i] for j in range(len(problems)))
    if operation == "*":
        res = 1
        for row in problems:
            res *= row[i]
        total += res


print(f"The sum of the answers is {total}")
