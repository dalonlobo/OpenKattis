#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()
idx = 0

while idx < len(ip):
    count = int(ip[idx].strip())
    if count == -1:
        break
    prev_time = 0
    total_dist = 0
    for _ in range(count):
        idx += 1
        miles, time = [int(i) for i in ip[idx].strip().split()]
        total_dist += miles * (time - prev_time)
        prev_time = time
    print(f"{total_dist} miles")
    idx += 1
