from collections import defaultdict
import bisect

N = int(input())
A = list(map(int, input().split()))

T = sorted(set(A))
B = defaultdict(int)

for i in range(N):
    B[i] = bisect.bisect_left(T, A[i])
    B[i] += 1

for i in range(N):
    print(B[i], end=" ")
