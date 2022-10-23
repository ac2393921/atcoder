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


def pow(a, b):
    p = a
    ans = 1
    for i in range(30):
        wari = (1 << i)
        if (b // wari) % 2 == 1:
            ans = (ans * p) % MOD
        p = (p ** 2) % MOD
    return ans


def division(a, b):
    return (a * pow(b, MOD-2)) % MOD


def main():
    N, R = im()

    a = 1
    # 分子
    for i in range(1, N+1):
        a = (a * i) % MOD

    b = 1
    # 分母
    for i in range(1, R+1):
        b = (b*i) % MOD
    for i in range(1, N-R+1):
        b = (b*i) % MOD

    print(division(a, b))


if __name__ == "__main__":
    main()
