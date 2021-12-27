#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()[1:]

print(*ip[::-1], sep="", end="")
