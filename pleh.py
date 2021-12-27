#!/usr/bin/python3
import sys

try:
    white = sys.stdin.readline().strip().split(": ")[1].split(",")
except IndexError:
    white = []
try:
    black = sys.stdin.readline().strip().split(": ")[1].split(",")
except IndexError:
    black = []

cols = "abcdefgh"

def print_border() -> None:
    print("+" + "---+"*8)

def get_pawn(r: int, c:int) -> str:
    for val in black:
        h, i, j = val[0], val[-2], int(val[-1])
        if i == cols[c] and j == 8-r:
            if len(val) == 3:
                return h.lower()
            else:
                return "P"
    for val in white:
        h, i, j = val[0], val[-2], int(val[-1])
        if i == cols[c] and j == 8-r:
            if len(val) == 3:
                return h.upper()
            else:
                return "p"
    return ""

print_border()
for r in range(0, 8):
    row_print = "|"
    for c in range(0, 8):
        if (c + r) % 2 == 0:
            val = "...|"
        else:
            val = ":::|"
        pawn = get_pawn(r, c)
        if pawn:
            val = val[0] + pawn + val[-2:]
        row_print += val
    print(row_print)
    print_border()