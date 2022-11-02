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
def irl(N): return [list(im()) for _ in range(N)]
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
    def get_score(i, j):
        x1, y1 = XY[i]
        x2, y2 = XY[j]

        return ((x1-x2)**2 + (y1-y2) ** 2)**0.5

    N = ii()
    XY = irl(N)
    v = [0] * (N+1)
    print(1)
    v[1] = 1
    for i in range(N):
        min_s = INF
        tmp_i = -1
        for j in range(N):
            if i == j:
                continue
            if i == 0 or not v[j+1]:
                s = get_score(i, j)
                if s < min_s:
                    min_s = s
                    tmp_i = j+1
        if tmp_i >= 0:
            print(tmp_i)
        v[tmp_i] = 1
    print(1)


if __name__ == "__main__":
    main()
