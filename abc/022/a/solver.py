N, S, T = map(int, input().split())
W = int(input())
A = [int(input()) for _ in range(N - 1)]
ans = 0
if S <= W <= T:
    ans += 1
for i in range(len(A)):
    W += A[i]
    if S <= W <= T:
        ans += 1
print(ans)

