N = int(input())
A = list(map(int, input().split()))
l = []

for i in range(N):
    for j in range(len(l)):
        l[j] += A[i]
    l.append(A[i])

ans = 0
for i in range(len(l)):
    if l[i] >= 4:
        ans += 1
print(ans)
