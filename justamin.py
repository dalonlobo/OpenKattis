import sys

N = int(sys.stdin.readline().strip())
actual_min = 0
sl_min = 0

for _ in range(N):
    sl_time, actual_time = [int(i) for i in sys.stdin.readline().strip().split()]
    actual_min += actual_time
    sl_min += sl_time

sl_minutes = actual_min / (sl_min * 60)
if sl_minutes <= 1:
    print("measurement error")
else:
    print(sl_minutes)
