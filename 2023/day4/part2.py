import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

scores = []
cards = {}

def add_next_cards(card_num, score):
    for card in range(card_num+1, card_num+score+1):
        if cards.get(card):
            cards[card] += 1
        else:
            cards[card] = 1

for card_num, line in enumerate(lines, 1):
    line = re.sub(".*: ", "", line)

    numbers = line.split(" | ")
    winning = re.findall(r"\d+", numbers[0])
    owned_numbers = re.findall(r"\d+", numbers[1])
    winning = [int(num) for num in winning]
    owned_numbers = [int(num) for num in owned_numbers]

    score = 0

    for number in owned_numbers:
        if number in winning:
            score += 1

    this_card = cards.get(card_num)

    if this_card is not None:
        cards[card_num] += 1
    else:
        cards[card_num] = 1

    for _ in range(cards[card_num]):
        add_next_cards(card_num, score)


print(f"The number of scratchcards is: {sum(cards.values())}")
