from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

cnt = 1
d = defaultdict(int)
B = sorted(A)
for i in range(N):
    if not d[B[i]]:
        d[B[i]] = cnt
        cnt += 1

for i in range(N):
    print(d[A[i]], end=" ")
