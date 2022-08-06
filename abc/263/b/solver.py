from collections import defaultdict

N = int(input())
P = list(map(int, input().split()))
d = defaultdict(int)
for i in range(N - 1):
    d[i + 2] = P[i]

ans = 0
n = N
while n != 1:
    ans += 1
    n = d[n]
print(ans)
