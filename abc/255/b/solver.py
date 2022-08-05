import math

n, k = [int(v) for v in input().split()]
ik = [int(v) - 1 for v in input().split()]
A = [[int(v) for v in input().split()] for _ in range(n)]
maximum = 0
for i, v in enumerate(A):
    if i not in ik:
        x, y = v
        min_A = 0
        min_i = 0
        min_l = 0
        for ii, j in enumerate(ik):
            xx, yy = A[j]
            length = math.sqrt((x - xx) ** 2 + (y - yy) ** 2)
            if ii == 0 or length < min_l:
                min_i = j
                min_l = length
        maximum = max(maximum, min_l)
print(maximum)
