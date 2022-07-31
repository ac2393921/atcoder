N, X, Y = map(int, input().split())
r = [0] * (N + 1)
b = [0] * (N + 1)
r[N] = 1

i = N
while i >= 2:
    r[i - 1] += r[i]
    b[i] += r[i] * X

    r[i - 1] += b[i]
    b[i - 1] = b[i] * Y

    i -= 1
print(b[1])