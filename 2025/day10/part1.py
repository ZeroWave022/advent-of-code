import os
import math
import time

path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

machines = []

for line in lines:
    parts = line.split(" ")
    config_text, buttons_text, reqs_text = parts[0], parts[1:-1], parts[-1]
    config = []
    for char in config_text[1:-1]:
        config.append(1 if char == "#" else 0)

    buttons = []
    for button in buttons_text:
        button = button[1:-1]
        buttons.append(tuple(int(i) for i in button.split(",")))

    machines.append(
        {
            "config": config,
            "buttons": buttons,
            "reqs": reqs_text,
        }
    )

cache = {}


def configure_machine(machine, state, steps):
    config = machine["config"]
    buttons = machine["buttons"]

    if (tuple(config), tuple(state), tuple(buttons)) in cache:
        return cache[tuple(config), tuple(state), tuple(buttons)]

    if config == state:
        return steps

    min_steps = math.inf

    for button in buttons:
        # No point in pressing the same button again,
        # as we would just end up in the same place again
        new_buttons = buttons.copy()
        new_buttons.remove(button)

        # Update the state for this new machine
        new_state = state.copy()
        for i in button:
            new_state[i] = 1 if new_state[i] == 0 else 0

        # Create new machine after having pressed the button
        # and calculate whether this solution is better
        new_machine = {
            "config": config,
            "buttons": new_buttons,
            "reqs": machine["reqs"],
        }
        min_steps = min(min_steps, configure_machine(new_machine, new_state, steps + 1))

    cache[tuple(config), tuple(state), tuple(buttons)] = min_steps
    return min_steps


total = sum(configure_machine(m, [0] * len(m["config"]), 0) for m in machines)

print(f"The fewest button presses to configure all machines is {total}")
