from collections import defaultdict

d = defaultdict(int)
A, B, C = map(int, input().split())
d[A] += 1
d[B] += 1
d[C] += 1

if d[5] == 2 and d[7] == 1:
    print("Yes")
else:
    print("No")
