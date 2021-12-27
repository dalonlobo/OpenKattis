#!/usr/bin/python3
import sys

ip = sys.stdin.readlines()
idx, set_count = 0, 1

while idx < len(ip):
    count = int(ip[idx].strip())
    if count == 0:
        break
    idx += 1
    inputs = [i.strip() for i in ip[idx : (idx + count)]]
    idx += count
    output = []
    if count % 2 != 0:
        output.append(inputs[-1])
        count -= 1
        inputs = inputs[:-1][::-1]
    else:
        inputs = inputs[::-1]
    i = 0
    while count > 0:
        output.insert(len(output), inputs[i])
        i += 1
        output.insert(0, inputs[i])
        i += 1
        count -= 2
    print(f"SET {set_count}")
    print(*output, sep="\n")
    set_count += 1
