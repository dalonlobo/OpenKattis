#!/usr/bin/python3
import sys

vars = {}
keys = {}

for line in sys.stdin:
    ip = line.strip()
    cmd = ip.split()[0]
    if cmd == "clear":
        del keys
        del vars
        keys, vars = {}, {}
    elif cmd == "def":
        _, var, val = ip.split()
        if var in vars.keys():
            del keys[int(vars[var])]
        vars[var] = int(val)
        keys[int(val)] = var
    elif cmd == "calc":
        vals = ip.split()
        calc = []
        try:
            for val in vals[1:-1]:
                if val in ["+", "-"]:
                    calc.append(val)
                else:
                    calc.append(str(vars[val]))
            print(" ".join(vals[1:] + [keys[eval(" ".join(calc))]]))
        except KeyError:
            print(" ".join(vals[1:] + ["unknown"]))
