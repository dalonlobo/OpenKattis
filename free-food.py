import sys

ip = sys.stdin.readlines()

testcases = int(ip[0])
currentidx = 1
food = []
for test in range(testcases):
    start, end = [int(_) for _ in ip[currentidx + test].split()]
    _tmp = [_ for _ in range(start, end + 1)]
    food += _tmp

print(len(set(food)))
