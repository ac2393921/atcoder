H, W, N = map(int, input().split())
Z = [[0] * (W+1) for _ in range(H+1)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    Z[A-1][B-1] += 1
    Z[C][D] += 1
    Z[A-1][D] -= 1
    Z[C][B-1] -= 1

for h in range(H+1):
    for w in range(1, W+1):
        Z[h][w] = Z[h][w] + Z[h][w-1]

for w in range(W+1):
    for h in range(1, H+1):
        Z[h][w] = Z[h][w] + Z[h-1][w]

for i in range(len(Z)-1):
    print(*Z[i][:-1])
