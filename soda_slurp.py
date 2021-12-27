#!/usr/bin/python3

e, f, c = [int(i) for i in input().strip().split()]

total = e + f
sodas = 0

while total >= c:
    sodas += 1
    total = total - c + 1

print(sodas)
