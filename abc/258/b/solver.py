N, K, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
L = list(map(int, input().split()))
d = [0] * (N + 1)
for i in range(1, K + 1):
    d[A[i]] = 1

for i in range(Q):
    c = A[L[i]]
    if c == N:
        continue

    if not d[c + 1]:
        d[c], d[c + 1] = d[c + 1], d[c]
        A[L[i]] = c + 1

print(*A[1:])
