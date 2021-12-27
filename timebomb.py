#!/usr/bin/python3
import sys

ascii0 = "**** ** ** ****"
ascii1 = "  *  *  *  *  *"
ascii2 = "***  *****  ***"
ascii3 = "***  ****  ****"
ascii4 = "* ** ****  *  *"
ascii5 = "****  ***  ****"
ascii6 = "****  **** ****"
ascii7 = "***  *  *  *  *"
ascii8 = "**** ***** ****"
ascii9 = "**** ****  ****"

ascii = [ascii0, ascii1, ascii2, ascii3, ascii4, ascii5, ascii6, ascii7, ascii8, ascii9]
given_ascii = [""] * 10

for _ in range(5):
    val = sys.stdin.readline().strip("\n")
    start, end = 0, 3
    for i in range(10):
        given_ascii[i] += val[start:end]
        start += 4
        end += 4

given_digit = ""
for val in given_ascii:
    if val:
        digit = False
        for i in range(10):
            if val == ascii[i]:
                given_digit += str(i)
                digit = True
                break
        if not digit:
            given_digit += "x"

if given_digit.isdigit():
    if int(given_digit) % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")
else:
    print("BOOM!!")
