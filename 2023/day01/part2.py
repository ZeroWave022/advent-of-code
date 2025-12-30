import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

numbers = []

words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def keep_possible_chars(word, exclude=None):
    check_against = words.copy()
    if exclude:
        check_against.pop(exclude)
    while True:
        word_is_possible = [w.startswith(word) for w in check_against]

        if not any(word_is_possible) and word != "":
            word = word[1:]
            continue

        break

    return word

for line in lines:
    line_num = ""
    word = ""
    for char in line:
        if char.isdigit():
            line_num += char
        else:
            word += char

        word = keep_possible_chars(word)

        if word in words:
            line_num += words[word]
            word = keep_possible_chars(word, word)

    numbers.append(int(line_num[0] + line_num[-1]))

print(f"The sum of all calibration values is: {sum(numbers)}")
