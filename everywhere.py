import sys

ip = sys.stdin.readlines()

testcases = int(ip[0])
currentidx = 1
for test in range(testcases):
    num_cities = int(ip[currentidx])
    currentidx += 1
    cities = []
    for i in range(num_cities):
        cities.append(ip[currentidx + i].strip())
    currentidx += num_cities
    print(len(set(cities)))
