from collections import defaultdict

A = int(input())
B = int(input())
C = int(input())
r = defaultdict(int)

for i, j in enumerate(sorted([A, B, C], reverse=True)):
    r[j] += i + 1

print(r[A])
print(r[B])
print(r[C])
