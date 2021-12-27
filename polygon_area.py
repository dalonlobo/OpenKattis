#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()
idx = 0

while idx < len(ip):
    n = int(ip[idx].strip())
    if n == 0:
        break
    idx += 1
    x, y = [], []
    for _ in range(n):
        a, b = [int(i) for i in ip[idx].strip().split()]
        x.append(a)
        y.append(b)
        idx += 1
    x.append(x[0])
    y.append(y[0])
    result = 0
    for i in range(n):
        result += (x[i + 1] - x[i]) * (y[i + 1] + y[i])
    if result >= 0:
        x = x[::-1]
        y = y[::-1]
    tmp1, tmp2 = 0, 0
    for i in range(n):
        tmp1 += x[i] * y[i + 1]
        tmp2 += y[i] * x[i + 1]
    area = abs((tmp2 - tmp1) / 2)
    if result >= 0:
        print(f"CW {area}")
    else:
        print(f"CCW {area}")
