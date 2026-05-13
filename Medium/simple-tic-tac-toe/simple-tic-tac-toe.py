game_state = input()

grid = [
    [x for x in game_state[0:3]],
    [x for x in game_state[3:6]],
    [x for x in game_state[6:9]],
]

print("---------")
for row in grid:
    line = "| " + " ".join(row) + " |"
    print(line)
print("---------")
