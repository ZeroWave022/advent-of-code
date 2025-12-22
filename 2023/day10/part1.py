import os

path = os.path.join(os.path.abspath(__file__), "../input.txt")

with open(path, encoding="utf-8") as f:
    lines = f.read().splitlines()

def find_start_pos(pipes):
    for row in pipes:
        if "S" in row:
            return (pipes.index(row), row.index("S"))

def find_start_pipes(start_pos, pipes):
    row, col = start_pos
    connected = []

    if pipes[row][col-1] in ["-", "L", "F"]:
        connected.append((row, col-1))

    if pipes[row][col+1] in ["-", "J", "7"]:
        connected.append((row, col+1))

    if pipes[row-1][col] in ["|", "7", "F"]:
        connected.append((row-1, col))

    if pipes[row+1][col] in ["|", "L", "J"]:
        connected.append((row+1, col))

    return connected

pipe_moves = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)]
}

pipe_map = []

for line in lines:
    pipe_map.append(tuple(line))

start_pos = find_start_pos(pipe_map)
start_pipes = find_start_pipes(start_pos, pipe_map)

pos = start_pipes[0]
pos_his = [start_pos, pos]

# Starting at the first pipe after the start, so count from 1
moves_num = 1

while True:
    row, col = pos
    moves = pipe_moves[pipe_map[row][col]]

    moved = False

    for move in moves:
        possible_move = (pos[0]+move[0], pos[1]+move[1])
        if possible_move not in pos_his:
            pos = possible_move
            pos_his.append(possible_move)
            moved = True
            break

    moves_num += 1

    if not moved:
        break

print(f"The point farthest from the loop start is {moves_num / 2} moves away.")
