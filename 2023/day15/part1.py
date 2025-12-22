import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    steps = f.read().split(",")

def convert_to_HASH(text):
    val = 0
    for char in text:
        val += ord(char)
        val = (val * 17) % 256

    return val

total = 0

for step in steps:
    total += convert_to_HASH(step)

print(f"The sum of the HASH results is: {total}")
