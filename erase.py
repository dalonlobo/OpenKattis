#!/usr/bin/python3
import sys

N = int(sys.stdin.readline().strip())

before = sys.stdin.readline().strip()
after = sys.stdin.readline().strip()

if N % 2 == 0:
    if before == after:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    failed = False
    for i in range(len(before)):
        if before[i] == after[i]:
            failed = True
            break
    if failed:
        print("Deletion failed")
    else:
        print("Deletion succeeded")
