import sys
from itertools import combinations

# ip = sys.stdin.readlines()

inputs = [int(i.strip()) for i in sys.stdin.readlines()]

for comb in combinations(inputs, 7):
    if sum(comb) == 100:
        print(*comb, sep="\n")
        break
