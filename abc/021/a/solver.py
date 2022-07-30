N = int(input())
d = {1: 0, 2: 0, 4: 0, 8: 0}
cnt = 0
for i in [8, 4, 2, 1]:
    d[i] += N // i
    N -= i * d[i]
    cnt += d[i]

print(cnt)

for k, v in d.items():
    for i in range(v):
        print(k)
