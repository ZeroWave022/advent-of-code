import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

scores = []

for line in lines:
    line = re.sub(".*: ", "", line)

    numbers = line.split(" | ")
    winning = re.findall(r"\d+", numbers[0])
    owned_numbers = re.findall(r"\d+", numbers[1])
    winning = [int(num) for num in winning]
    owned_numbers = [int(num) for num in owned_numbers]

    score = 0

    for number in owned_numbers:
        if number in winning:
            if score == 0:
                score += 1
            else:
                score *= 2

    if score:
        scores.append(score)

print(f"The sum of the scores on the scratchcards is: {sum(scores)}")
