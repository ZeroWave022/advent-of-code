import os
import re

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

hands = {
    "high": [],
    "one-pair": [],
    "two-pair": [],
    "three": [],
    "full-house": [],
    "four": [],
    "five": [],
}

for line in lines:
    unique_chars = list(set(line[:5]))
    occurances = [line[:5].count(c) for c in unique_chars]

    if 5 in occurances:
        hand_type = "five"
    elif 4 in occurances:
        hand_type = "four"
    elif 3 in occurances and 2 in occurances:
        hand_type = "full-house"
    elif 3 in occurances:
        hand_type = "three"
    elif occurances.count(2) == 2:
        hand_type = "two-pair"
    elif 2 in occurances:
        hand_type = "one-pair"
    else:
        hand_type = "high"

    hands[hand_type].append({
        "hand": line[:5],
        "bid": int(re.findall(r"\d+", line)[-1])
    })

char_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def order_hands(hands: list[dict], from_index: int, ordered = None):
    check_index = from_index
    if not ordered:
        ordered = []

    while len(hands) >= 1:
        next_char_value = []

        for hand in hands:
            next_char = hand["hand"][check_index]
            next_char_value.append(char_values[next_char])

        min_value = min(next_char_value)
        min_count = next_char_value.count(min_value)

        if min_count > 1 and min_count == len(hands):
            check_index += 1
        elif min_count > 1:
            min_hands = []
            for i, char_value in enumerate(next_char_value):
                if char_value == min_value:
                    min_hands.append(hands[i])

            ordered = order_hands(min_hands, check_index+1, ordered)
        else:
            worst_hand_index = next_char_value.index(min_value)
            ordered.append(hands[worst_hand_index])
            # del hands[worst_hand_index]

        for ordered_hand in ordered:
            if ordered_hand in hands:
                del hands[hands.index(ordered_hand)]

    return ordered

def order_same_type_hands(hands: list[dict]):
    ordered = []
    for card in char_values.keys():
        have_same_card = [hand for hand in hands if hand["hand"][0] == card]

        if len(have_same_card) == 1:
            ordered.append(have_same_card[0])
            continue

        ordered.extend(order_hands(have_same_card, 1))

    return ordered

all_hands = []

for same_type_hands in hands.values():
    if len(same_type_hands) > 1:
        ordered = order_same_type_hands(same_type_hands)
        all_hands.extend(ordered)
    elif len(same_type_hands) == 1:
        all_hands.append(same_type_hands[0])

total_wins = 0

for i, hand in enumerate(all_hands, 1):
    total_wins += hand["bid"] * i

print(total_wins)
