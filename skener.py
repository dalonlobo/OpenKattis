#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()

r, c, zr, zc = [int(i) for i in ip[0].strip().split()]

for line in ip[1:]:
    line = line.strip()
    for _ in range(zr):
        print("".join([ch * zc for ch in line]))
