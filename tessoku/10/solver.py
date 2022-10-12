n = int(input())
a = list(map(int, input().split()))
d = int(input())

p = [0] * n
q = [0] * n

p[0] = a[0]
for i in range(1, n):
    p[i] = max(p[i-1], a[i])

q[n-1] = a[n-1]
for i in range(n-2, -1, -1):
    q[i] = max(q[i+1], a[i])

for d in range(d):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    print(max(p[l-1], q[r+1]))
