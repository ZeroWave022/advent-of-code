import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

num_batteries = 12
total = 0

for bank in lines:
    nums = [int(battery) for battery in list(bank)]

    # Select the last 12 batteries
    max_batteries = nums[-num_batteries:]
    from_index = 0
    to_index = len(nums) - num_batteries

    # For the remaining batteries to the left of the last 12,
    # we attempt to improve the score by selecting a better battery
    # that's the farthest to the left
    for i in range(num_batteries):
        checking = nums[from_index:to_index]
        max_value = max(checking)

        # If none of the batteries to the left of the selected ones
        # are better than the most significant battery,
        # then there's no way to further improve the joltage
        if max_value < max_batteries[i]:
            break

        max_batteries[i] = max_value
        from_index += checking.index(max_value) + 1
        to_index += 1

    total += int("".join(str(battery) for battery in max_batteries))


print(f"Total output joltage is {total}")
