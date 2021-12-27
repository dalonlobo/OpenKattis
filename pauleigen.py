#!/usr/bin/python3
import sys

ip = [int(i) for i in sys.stdin.readline().strip().split()]

if ((ip[1] + ip[2]) // ip[0]) % 2 == 0:
    print("paul")
else:
    print("opponent")
