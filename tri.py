import sys

inputs = [int(i) for i in sys.stdin.readline().strip().split()]

operations = ["+", "-", "*", "/"]

for op in operations:
    if int(eval(f"{inputs[0]}{op}{inputs[1]}")) == inputs[2]:
        print(f"{inputs[0]}{op}{inputs[1]}={inputs[2]}")
        break
    if int(eval(f"{inputs[1]}{op}{inputs[2]}")) == inputs[0]:
        print(f"{inputs[0]}={inputs[1]}{op}{inputs[2]}")
        break
