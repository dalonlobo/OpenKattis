#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()

for i in range(int(ip[0].strip())):
    print(f"{i+1} Abracadabra")
