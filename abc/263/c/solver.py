import itertools

N, M = map(int, input().split())
S = [str(i) for i in range(1, M + 1)]
for i in itertools.combinations(S, N):
    print(*i)

