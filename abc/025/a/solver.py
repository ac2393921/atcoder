from itertools import product

S = input()
N = int(input())
d = [c for c in product(S, repeat=2)]
print("".join(d[N - 1]))
