from collections import defaultdict

C = list(map(int, input().split()))
d = defaultdict(int)

for c in C:
    d[c] += 1

fg_3 = False
fg_2 = False
for k, v in d.items():
    if v == 3:
        fg_3 = True

    if v == 2:
        fg_2 = True
print("Yes" if fg_2 and fg_3 else "No")
