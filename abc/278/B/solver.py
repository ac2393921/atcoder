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


def is_in_24_hours(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59


def misjudged(h, m):
    A, B = h // 10, h % 10
    C, D = m // 10, m % 10
    AC = A * 10 + C
    BD = B * 10 + D
    return is_in_24_hours(AC, BD)


def main():
    H, M = im()
    while not misjudged(H, M):
        M += 1
        if M == 60:
            H, M = H + 1, 0
        if H == 24:
            H = 0
    print(H, M)


if __name__ == "__main__":
    main()
