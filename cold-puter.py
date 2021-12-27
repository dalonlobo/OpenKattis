import sys

ip = sys.stdin.readlines()

count = 0
for val in ip[1].split():
    val = int(val)
    if val < 0:
        count += 1

print(count)
