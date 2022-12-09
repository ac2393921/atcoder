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
    A = srl(N)

    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]

    ans = 0
    for x in range(N):
        for y in range(N):
            for i in range(8):
                tmp = A[x][y]
                for j in range(N-1):
                    x = (x + dx[i]) % N
                    y = (y + dy[i]) % N

                    tmp += A[x][y]

                ans = max(ans, int(tmp))

    print(ans)


if __name__ == "__main__":
    main()
