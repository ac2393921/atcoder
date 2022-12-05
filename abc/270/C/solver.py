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
    N, X, Y = im()
    to = defaultdict(list)
    for _ in range(N-1):
        u, v = im()
        to[u].append(v)
        to[v].append(u)

    ans = []

    def dfs(v, p=-1):
        if v == X:
            ans.append(v)
            return True
        for u in to[v]:
            if u == p:
                continue
            if (dfs(u, v)):
                ans.append(v)
                return True

        return False

    dfs(Y)
    print(*ans)


if __name__ == "__main__":
    main()
