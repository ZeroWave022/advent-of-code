import os
from time import sleep
from rich.text import Text
from rich.console import Console


def show_nums(show_checking: bool = True):
    nums_text = Text(style="bold")

    for index, num in enumerate(nums):
        if index in range(from_index, to_index) and show_checking:
            nums_text.append(str(num), style="yellow")
            continue
        if index in selected:
            nums_text.append(str(num), style="green")
        else:
            nums_text.append(str(num))

    console.print(nums_text)


def show_search_status():
    console.clear()
    console.print(title)
    console.print(search_text)
    show_nums()


def show_summary():
    console.clear()
    console.print(title)
    console.print("Done! Selected the following:")
    show_nums(False)
    console.print(f"Current total is: {total}")


path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()


num_batteries = 12
total = 0

console = Console()
title = Text("Advent of Code 2025 - Day 3 (Part 2)", style="bold gold3")
search_text = Text("Searching for ")
search_text.append("better batteries", style="bold yellow")
search_text.append("...")

count = 0

for bank in lines:
    console.clear()
    console.print(title)
    nums = [int(battery) for battery in list(bank)]

    # Select the last 12 batteries
    max_batteries = nums[-num_batteries:]
    from_index = 0
    to_index = len(nums) - num_batteries
    selected = list(range(len(nums) - num_batteries, len(nums)))

    console.print("Selecting last 12 batteries...")
    first = [str(num) for num in nums[:-num_batteries]]
    last = [str(num) for num in nums[-num_batteries:]]
    nums_text = Text("".join(first), style="bold")
    nums_text.append("".join(last), style="green")
    console.print(nums_text)

    sleep(3 if count < 3 else 0.1)

    # For the remaining batteries to the left of the last 12,
    # we attempt to improve the score by selecting a better battery
    # that's the farthest to the left
    for i in range(num_batteries):
        checking = nums[from_index:to_index]
        max_value = max(checking)

        show_search_status()
        sleep(0.5 if count < 3 else 0.1)

        # If none of the batteries to the left of the selected ones
        # are better than the most significant battery,
        # then there's no way to further improve the joltage
        if max_value <= max_batteries[i]:
            break

        max_batteries[i] = max_value
        selected.remove(len(nums) - num_batteries + i)
        from_index += checking.index(max_value) + 1
        selected.append(from_index - 1)
        to_index += 1

    total += int("".join(str(battery) for battery in max_batteries))

    show_summary()
    sleep(3 if count < 3 else 0.5)
    count += 1

    if count == 3:
        console.clear()
        console.print(title)
        console.print(Text("Speeding up!", style="bold red"))
        sleep(2)


console.print(f"Total output joltage is {total}")
