from collections import defaultdict

N, M = map(int, input().split())
X = [0] + list(map(int, input().split()))
CY = defaultdict(int)
for _ in range(M):
    c, y = map(int, input().split())
    CY[c] = y

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(N + 1):
        now = 0
        if i < j:
            continue
        if j == 0:
            for k in range(N + 1):
                now = max(now, dp[i - 1][k])
        else:
            now = dp[i - 1][j - 1] + X[i] + CY[j]
        dp[i][j] = now

ans = 0
for j in range(N + 1):
    ans = max(ans, dp[N][j])
print(ans)
