N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# accumulate[i] = A[0] + A[1] + ... A[i-1]
accumulate = [0]
for element in A:
    accumulate.append(accumulate[-1] + element)

left = [l * L - accumulate[l] for l in range(N + 1)]
right = [(N - r) * R + accumulate[r] for r in range(N + 1)]

right_min = right
for i in range(N - 1, -1, -1):
    right_min[i] = min(right_min[i], right_min[i + 1])

ans = L * N

for l in range(N + 1):
    tmp = left[l] + right_min[l]
    ans = min(ans, tmp)

print(ans)
