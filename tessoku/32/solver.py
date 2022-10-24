import math
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
def ir(n): return [ii() for _ in range(n)]
def irl(n): return [il() for _ in range(n)]
def si(): return input()
def sm(): return input().split()
def sl(): return list(sm())
def sr(n): return [si for _ in range(n)]
def srs(n): return [sl() for _ in range(n)]
def srl(n): return [list(si()) for _ in range(n)]
def lcm(a, b): return a * b // gcd(a, b)


sys.setrecursionlimit(10 ** 6)
inf = float('inf')
mod = 10 ** 9 + 7


def main():
    N, A, B = im()
    dp = [0]*(N+1)

    for i in range(N+1):
        if i >= A and not dp[i-A]:
            dp[i] = 1
        elif i >= B and not dp[i-B]:
            dp[i] = 1

    print("First" if dp[N] else "Second")


if __name__ == "__main__":
    main()
