#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()

for val in ip:
    a, b = [int(i) for i in val.strip().split()]
    print(abs(a - b))
