from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
    S = input()
    if d[S]:
        print(f"{S}({d[S]})")
    else:
        print(S)
    d[S] += 1
