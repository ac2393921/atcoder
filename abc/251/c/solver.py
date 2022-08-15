from collections import defaultdict

N = int(input())
max_t = 0
ans = 0
d = defaultdict(int)
for i in range(1, N + 1):
    s, t = map(str, input().split())
    t = int(t)
    if d[s]:
        continue
    if max_t < t:
        max_t = t
        ans = i
    d[s] = 1
print(ans)
