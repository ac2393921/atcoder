A = list(map(int, input().split()))
A = sorted(A)
ans = 0
for i in range(1,3):
    ans += abs(A[i]-A[i-1])
print(ans)