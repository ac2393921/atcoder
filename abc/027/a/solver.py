from collections import defaultdict

d = defaultdict(int)
l = list(map(int, input().split()))
for i in range(3):
    d[l[i]] += 1
for k, v in d.items():
    if v == 1:
        print(k)
    if v == 3:
        print(k)
