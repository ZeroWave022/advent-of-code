import os

equivalent = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

wins_against = {
    "Z": "A",
    "X": "B",
    "Y": "C"
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

def determine_game(you: str, opponent: str) -> bool | int:
    """A function to check whether a rock, paper, scissors game is won, lost or a draw.
    
    you: X for rock, Y for paper and Z for scissors
    opponent: A for rock, B for paper and C for scissors

    Returns True if game is won, False if game is lost and -1 if the game is a draw.
    """
    if equivalent[you] == opponent:
        return -1

    if wins_against[you] == opponent:
        return False

    return True

path = os.path.join(".", "day_2_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

games: list[list[str]] = []

for line in raw_data:
    games.append(line.split(" "))

total_points = 0

for game in games:
    result = determine_game(game[1], game[0])

    total_points += points_for_choosing[game[1]]

    if result == -1:
        total_points += points_for_result["draw"]
    elif result is True:
        total_points += points_for_result["win"]
    else:
        total_points += points_for_result["loss"]

print(total_points)
