ip = input()

index = [1, 0, 0]
for move in ip:
    if move == "A":
        index[0], index[1] = index[1], index[0]
    elif move == "B":
        index[1], index[2] = index[2], index[1]
    elif move == "C":
        index[2], index[0] = index[0], index[2]

print(index.index(1) + 1)
