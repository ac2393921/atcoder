n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = set()
a = []
for i in range(n):
    a.append((-A[i], i + 1))
a.sort()
for i in range(x):
    S.add(a[i][1])
a = []
for i in range(n):
    a.append((-B[i], i + 1))
count = 0
a.sort()
for i in range(n):
    if y == 0:
        break
    if a[i][1] in S:
        continue
    S.add(a[i][1])
    count += 1
    if count == y:
        break
a = []
for i in range(n):
    a.append((-(A[i] + B[i]), i + 1))
count = 0
a.sort()
for i in range(n):
    if z == 0:
        break
    if a[i][1] in S:
        continue
    S.add(a[i][1])
    count += 1
    if count == z:
        break
b = list(S)
b.sort()
for i in range(len(b)):
    print(b[i])
