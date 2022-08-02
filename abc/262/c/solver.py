N = int(input())
A = list(map(int, input().split()))
ans = 0
same_idx = 0
dif_cnt = 0
d = {a: i + 1 for i, a in enumerate(A)}

for i in range(N):
    # if A[A[i]-1] > A[i]:
    #     print(A[A[i]], A[i])
    if A[i] == i + 1:
        same_idx += 1
    elif A[A[i]-1] > A[i] and d[A[A[i]]] == i + 1:
        dif_cnt += 1

print(same_idx, dif_cnt)
