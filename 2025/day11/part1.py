import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

outputs = {}

for line in lines:
    name, device_outputs = line.split(": ")
    outputs[name] = device_outputs.split(" ")

paths = 0
queue = outputs["you"].copy()

while len(queue) != 0:
    device = queue.pop()
    if device == "out":
        paths += 1
        continue
    queue.extend(outputs[device])


print(f"The number of paths is {paths}")
