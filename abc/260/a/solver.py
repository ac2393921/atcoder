from collections import defaultdict

d = defaultdict(int)
S = input()
for i in range(3):
    d[S[i]] += 1
for k, v in d.items():
    if v == 1:
        print(k)
        exit()
print(-1)
