from collections import defaultdict

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
V = defaultdict(int)
for _ in range(M):
    X, Y = map(int, input().split())
    V[X - 1] = Y

for i in range(N - 1):
    T += V[i]
    if 0 >= T - A[i]:
        print("No")
        exit()
    T -= A[i]
print("Yes")
