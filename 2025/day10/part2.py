import os
import numpy as np
from scipy.optimize import milp, LinearConstraint

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

    reqs = [int(i) for i in reqs_text[1:-1].split(",")]

    machines.append(
        {
            "config": config,
            "buttons": buttons,
            "reqs": reqs,
        }
    )


def configure_machine(machine):
    # Observation: If every button is assigned a variable x_i,
    # we can create a system of equations that we can solve.
    # By minimizing all the x_i values, we will get the optimum solution

    # Start with empty coefficients for each equation (row in our equations system)
    coefficients = np.zeros((len(machine["reqs"]), len(machine["buttons"])))

    # The expected answer to each equation is the joltage requirement
    expected = np.array(machine["reqs"])

    x_i = 0
    for button in machine["buttons"]:
        for j in button:
            coefficients[j][x_i] = 1
        x_i += 1

    # We want to minimize the number of any and all buttons.
    # The coefficient of each is 1
    c = [1] * len(machine["buttons"])

    solution = milp(
        c=c,
        constraints=LinearConstraint(coefficients, expected, expected),
        # Each of the variables is an integer.
        # This needs to be specified by providing an array
        # of values 0 to 3, where 1 means integer.
        # We happen to already have such an array, so we reuse it here
        integrality=c,
    )

    return sum(solution.x)


total = int(sum(configure_machine(m) for m in machines))

print(f"The fewest button presses to configure all machines is {total}")
