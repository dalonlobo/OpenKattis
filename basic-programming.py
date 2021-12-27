#!/usr/bin/python3
import sys

N, t = [int(i) for i in sys.stdin.readline().strip().split()]
A = [int(i) for i in sys.stdin.readline().strip().split()]

if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    print(sorted(A[:3])[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    print(sum([i for i in A if i % 2 == 0]))
elif t == 6:
    print("".join([chr((i % 26) + 97) for i in A]))
elif t == 7:
    i = A[0]
    prev = i
    if max(A) < N - 1:
        print("Cyclic")
    else:
        while True:
            if i > N - 1:
                print("Out")
                break
            elif i == N - 1:
                print("Done")
                break
            elif i == A[i]:
                print("Cyclic")
                break
            elif prev == A[i]:
                print("Cyclic")
                break
            else:
                prev = i
                i = A[i]
