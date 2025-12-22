import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def convert_game_to_data(data) -> list:
    game_rounds = []

    for game in data.split(";"):
        this_round = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for color_data in game.split(", "):
            number = re.findall(r"\d+", color_data)[0]
            color_name = re.sub(r"\d+ ", "", color_data).strip()

            this_round[color_name] += int(number)

        game_rounds.append(this_round)

    return game_rounds

all_games = {}

for num, line in enumerate(lines, 1):
    line = re.sub(r"Game \d+: ", "", line)
    all_games[str(num)] = convert_game_to_data(line)

game_powers = []

for game_num, game in all_games.items():
    mins = {
        "red": 999,
        "green": 999,
        "blue": 999
    }

    max_red = max([r["red"] for r in game])
    max_green = max([r["green"] for r in game])
    max_blue = max([r["blue"] for r in game])

    game_powers.append(max_red * max_green * max_blue)


print(f"The sum of the game powers is: {sum(game_powers)}")
