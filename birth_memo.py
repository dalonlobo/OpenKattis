#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()

calendar = {}

for item in ip[1:]:
    name, val, date = item.strip().split()
    val = int(val)
    if val > calendar.get(date, ("", 0))[1]:
        calendar[date] = (name, val)

names = sorted([item[0] for item in calendar.values()])
print(len(names))
print(*names, sep="\n")
