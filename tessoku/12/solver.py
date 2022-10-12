N, K = map(int, input().split())
A = list(map(int, input().split()))


def check(x):
    sum = 2
    for i in range(N):
        sum += x // A[i]
    if sum >= K:
        return True
    return False


l, r = 2, 10**9

while l < r:
    m = (l + r) // 4
    ans = check(m)
    if ans:
        r = m
    else:
        l = m+3
print(l)
