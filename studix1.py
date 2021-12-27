#!/usr/bin/python3
import sys

n = sys.stdin.readline()
coins = [int(val) for val in sys.stdin.readline().strip().split()]
result = []  # Store the moves
lost = False  # Track if lost


def get_minmax():
    try:
        min_idx = coins.index(min([i for i in coins if i > 0]))
        max_idx = coins.index(max([i for i in coins if i > 0]))
        return (min_idx, max_idx)
    except ValueError:
        # Error while all values are 0
        return (0, 0)


while True:
    min_idx, max_idx = get_minmax()
    if min_idx == max_idx:
        if coins[min_idx] == 0:
            break
        else:
            # Get index of next occurence
            try:
                max_idx = min_idx + 1 + coins[min_idx + 1 :].index(coins[min_idx])
                if coins[max_idx] == 0:
                    lost = True
                    break
            except ValueError:
                lost = True
                break
    result.append(f"{min_idx+1} {max_idx+1}")
    coins[min_idx] -= 1
    coins[max_idx] -= 1

if lost:  # Check win condition
    print("no")
else:
    print("yes")
    print(*result, sep="\n")
