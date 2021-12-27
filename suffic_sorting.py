import sys

ip = sys.stdin.readlines()

line_idx = 0

while line_idx < len(ip):
    s = ip[line_idx].strip()

    suffixes = [int(i) for i in ip[line_idx + 1].split()[1:]]

    suf_dict = {}
    for idx in range(len(s)):
        suf_dict[s[idx:]] = idx

    resp = sorted(suf_dict.items())
    print(*[resp[i][1] for i in suffixes], sep=" ")
    line_idx += 2
