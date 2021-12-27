#!/usr/bin/python3
import sys
from fractions import Fraction

ip = sys.stdin.readlines()

vals = [int(i) for i in ip[1].strip().split()]

for val in vals[1:]:
    _tmp = Fraction(vals[0], val)
    print(f"{_tmp.numerator}/{_tmp.denominator}")
