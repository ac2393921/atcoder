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
    A = il()
    tmp = A[0]
    d = [0] * N
    d2 = [0] * N
    d3 = [0] * N

    for i in range(N):
        tmp = A[i]
        while True:
            if tmp % 2 == 0:
                tmp //= 2
                d2[i] += 1
            else:
                break

        while True:
            if tmp % 3 == 0:
                tmp //= 3
                d3[i] += 1
            else:
                break

        d[i] = tmp

    if len(set(d)) != 1:
        print(-1)
        exit()

    ans = 0

    def f(x):
        cnt = 0
        min_x = min(x)
        for i in range(N):
            cnt += x[i] - min_x
        return cnt

    ans += f(d2)
    ans += f(d3)
    print(ans)


if __name__ == "__main__":
    main()
