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
    def dfs(v, G, seen):
        seen[v] = True
        for v2 in G[v]:
            if seen[v2]:
                continue
            dfs(v2, G, seen)
        return

    N, M = im()
    G = [[] for _ in range(N+1)]
    for i in range(M):
        v, u = im()
        G[v].append(u)
        G[u].append(v)

    seen = [False for _ in range(N+1)]
    ans = 0

    for v in range(1, N+1):
        if seen[v]:
            continue
        dfs(v, G, seen)
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
