import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    steps = f.read().split(",")

def convert_to_HASH(text):
    val = 0
    for char in text:
        val += ord(char)
        val = (val * 17) % 256

    return val

def add_lens_to_box(label, length):
    if not boxes.get(current_box):
        boxes[current_box] = []

    labels_in_box = [lens["label"] for lens in boxes[current_box]]

    if label in labels_in_box:
        index = labels_in_box.index(label)
        boxes[current_box][index]["length"] = int(length)
    else:
        boxes[current_box].append({ "label": label, "length": int(length) })

def remove_label_from_box(label):
    if not boxes.get(current_box):
        return

    for lens in boxes[current_box]:
        if lens["label"] == label:
            boxes[current_box].remove(lens)

boxes = {}

for step in steps:
    current_box = str(convert_to_HASH(re.findall(r"[^-=]+", step)[0]))

    if "=" in step:
        label, length = step.split("=")
        add_lens_to_box(label, length)

    if "-" in step:
        label = step.split("-")[0]
        remove_label_from_box(label)

total = 0

for box_num, contents in boxes.items():
    if len(contents) == 0:
        continue

    for lens in contents:
        total += (int(box_num) + 1) * (contents.index(lens) + 1) * lens["length"]

print(f"Total focusing power of the lens is: {total}")
