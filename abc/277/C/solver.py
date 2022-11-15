import sys
import re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def ii(): return int(input())
def im(): return map(int, input().split())
def il(): return list(im())
def ir(N): return [ii() for _ in range(N)]
def irl(N): return [il() for _ in range(N)]
def si(): return input()
def sm(): return input().split()
def sl(): return list(sm())
def sr(N): return [si for _ in range(N)]
def srs(N): return [sl() for _ in range(N)]
def srl(N): return [list(si()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)


sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = ii()
    G = defaultdict(list)
    for _ in range(N):
        A, B = im()
        G[A].append(B)
        G[B].append(A)

    ans = 1
    q = deque()
    q.append(1)
    s = {1}
    while q:
        f = q.pop()
        for i in range(len(G[f])):
            nexf = G[f][i]
            if not nexf in s:
                ans = max(ans, nexf)
                q.append(nexf)
                s.add(nexf)

    print(ans)


if __name__ == "__main__":
    main()
