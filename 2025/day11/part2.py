import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

outputs = {}

for line in lines:
    name, device_outputs = line.split(": ")
    outputs[name] = device_outputs.split(" ")

outputs["out"] = []

paths = {}


def num_of_paths(device, dac, fft):
    dac = dac or device == "dac"
    fft = fft or device == "fft"

    if (device, dac, fft) in paths:
        return paths[(device, dac, fft)]

    if device == "out" and dac and fft:
        return 1

    total = 0

    for output in outputs[device]:
        total += num_of_paths(output, dac, fft)

    paths[(device, dac, fft)] = total
    return total


print(
    f"Total number of paths visiting dac and fft is {num_of_paths("svr", False, False)}"
)
