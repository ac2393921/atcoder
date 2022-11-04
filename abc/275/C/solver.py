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
from itertools import combinations
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


def check(x, y):
    v = []
    for i in range(4):
        for j in range(i):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            v.append(dx * dx + dy * dy)

    v = sorted(v)
    l = v[0]
    if l == 0:
        return False
    return v[0] == l and v[1] == l and v[2] == l and v[3] == l and v[4] == l*2 and v[5] == l*2


def main():
    S = srl(9)
    XY = [(i+1, j+1) for i in range(9) for j in range(9) if S[i][j] == "#"]

    ans = 0

    for xy in combinations(XY, 4):
        x = [xy[0][0], xy[1][0], xy[2][0], xy[3][0]]
        y = [xy[0][1], xy[1][1], xy[2][1], xy[3][1]]

        if check(x, y):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
