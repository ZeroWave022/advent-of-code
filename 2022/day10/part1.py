import os

path = os.path.join(os.path.dirname(__file__), "day_10_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

x = 1
global_cycle = 0
temp_cycle = 0

signals = []

def add_cycle():
    if (global_cycle - 20) % 40 == 0:
        signals.append(x * global_cycle)

for instruction in raw_data:
    if instruction == "noop":
        global_cycle += 1
        add_cycle()
        continue

    inc = int(instruction.split(" ")[-1])

    for i in range(2):
        global_cycle += 1
        add_cycle()

    x += inc

print(f"The sum of the signal strenghts is: {sum(signals)}")
