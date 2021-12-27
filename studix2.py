#!/usr/bin/python3
import sys

# Read the inputs
l, a, b, t, r = [int(val) for val in sys.stdin.readline().strip().split()]
n = int(sys.stdin.readline().strip())
carts = [int(val) for val in sys.stdin.readline().strip().split()]
# Add the final point carts
carts += [l]
selected_carts = []  # coffee carts selected
dp = {}  # save the time if started from this cart


def get_time(i, j):
    dist = carts[j] - carts[i]
    total_dist = (a * t) + (b * r)  # Distance travelled at end of drinking

    # Finished drinking coffee
    if dist >= total_dist:
        return t + r + ((dist - total_dist) / t)
    # Started drinking coffee
    if dist >= (a * t):
        return t + ((dist - (a * t)) / r)
    # Did not start drinking coffee
    return dist / t


def select_cart(start, i):
    # if i == n - 1 or (carts[i] + (a * t) + (b * r)) >= carts[n]:
    #     return get_time(i, n)
    # Divide time into 3 category, before drink, while drink, after drink
    e, f, g = 0, 0, 0
    before = get_time(e, n)
    drink = get_time(f, n)
    after = get_time(g, n)
    if after < before and after < drink:
        selected_carts.append(e)
    elif before < after and before < drink:
        selected_carts.append(f)
    else:
        selected_carts.append(g)


if n == 0:  # Edge case
    print(len(selected_carts))
elif n == 1:
    print(1)
    print(0)
elif n >= 2:
    selected_carts.append(0)  # First cart is always selected
    select_cart(carts[0], 1)  # Start selection process from 0
    # Print results
    print(len(selected_carts))
    if selected_carts:
        print(*selected_carts, sep=" ")
