import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

total = 0

for bank in lines:
    nums = [int(battery) for battery in list(bank)]
    max_joltage = 0
    for index, first in enumerate(nums):
        for second in nums[index + 1 :]:
            max_joltage = max(first * 10 + second, max_joltage)

    total += max_joltage

print(f"Total output joltage is {total}")
