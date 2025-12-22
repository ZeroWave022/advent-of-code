import os

path = os.path.join(os.path.dirname(__file__), "day_10_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

x = 1
global_cycle = 0
temp_cycle = 0

screen = [("." * 40) for _ in range(6)]

def draw_pixel():
    row = (global_cycle) // 40
    x_pos = global_cycle - row*40
    if x_pos in range(x-1, x+2):
        screen[row] = screen[row][:x_pos] + "#" + screen[row][x_pos+1:]

for instruction in raw_data:
    if instruction == "noop":
        draw_pixel()
        global_cycle += 1
        continue

    inc = int(instruction.split(" ")[-1])

    for i in range(2):
        draw_pixel()
        global_cycle += 1

    x += inc

print("The CRT screen is displaying:")
print("\n".join(screen))
