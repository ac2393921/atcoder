N = int(input())

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(1, N):
    for j in range(i + 1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for i in range(N):
    print(*[j for j in dp[i] if j != 0])
