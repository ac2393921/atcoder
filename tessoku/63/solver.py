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
    N, M = im()
    G = defaultdict(list)
    for i in range(M):
        A, B = im()
        G[A].append(B)
        G[B].append(A)

    d = [-1] * (N+1)
    T = deque()

    for i in range(N):
        T.append(1)
        d[1] = 0
        while T:
            pos = T.popleft()
            for j in range(len(G[pos])):
                to = G[pos][j]
                if d[to] == -1:
                    d[to] = d[pos] + 1
                    T.append(to)

    for i in range(1, N+1):
        print(d[i])


if __name__ == "__main__":
    main()
