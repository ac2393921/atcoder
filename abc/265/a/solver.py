X, Y, N = map(int, input().split())
ans = 10 ** 5
for i in range(100):
    for j in range(100):
        if i + j * 3 == N:
            ans = min(ans, (i * X) + (j * Y))
print(ans)
