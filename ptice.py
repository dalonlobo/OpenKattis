#!/usr/bin/python3

n = int(input().strip())
ans = [ch for ch in input().strip()]

a = ["A", "B", "C"]
b = ["B", "A", "B", "C"]
g = ["C", "C", "A", "A", "B", "B"]

scores = [0] * 3

for idx, ch in enumerate(ans):
    if a[idx % 3] == ch:
        scores[0] += 1
    if b[idx % 4] == ch:
        scores[1] += 1
    if g[idx % 6] == ch:
        scores[2] += 1

max_score = max(scores)

print(max_score)
if scores[0] == max_score:
    print("Adrian")
if scores[1] == max_score:
    print("Bruno")
if scores[2] == max_score:
    print("Goran")
