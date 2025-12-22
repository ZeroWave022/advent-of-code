import os

equivalent = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

wins_against = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

lost_against = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

# 1 point for choosing rock, 2 for choosing paper and 3 for choosing scissors
points_for_choosing = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

points_for_result = {
    "win": 6,
    "draw": 3,
    "loss": 0
}

def get_shape(opponent: str, result: str) -> str:
    """A function to get the shape needed to end a rock, paper, scissors game with the specified result.
    
    opponent: A for rock, B for paper and C for scissors
    result: Z for a win, X for a loss, Y for a draw

    Returns a string with the shape that needs to be played
    """
    if result == "X":
        return lost_against[opponent]
    elif result == "Y":
        return equivalent[opponent]

    return wins_against[opponent]

path = os.path.join(".", "day_2_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

games: list[list[str]] = []

for line in raw_data:
    games.append(line.split(" "))

total_points = 0

for game in games:
    shape = get_shape(game[0], game[1])

    total_points += points_for_choosing[shape]

    if game[1] == "X":
        total_points += points_for_result["loss"]
    elif game[1] == "Y":
        total_points += points_for_result["draw"]
    else:
        total_points += points_for_result["win"]

print(total_points)
