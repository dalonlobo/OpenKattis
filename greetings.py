#!/usr/bin/python3

greeting = input().strip()

print(greeting[0] + greeting[1:-1] * 2 + greeting[-1])
