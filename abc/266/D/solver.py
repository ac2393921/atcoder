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
    TXA = defaultdict(tuple)
    max_t = 10**5
    X = [0]*(max_t+1)
    A = [0]*(max_t+1)
    for i in range(N):
        t, x, a = im()
        X[t] = x
        A[t] = a

    dp = [[-INF] * (max_t+1) for _ in range(5)]
    dp[0][0] = 0

    for t in range(1, max_t+1):
        for x in range(5):
            dp[x][t] = dp[x][t-1]
            if x != 0:
                dp[x][t] = max(dp[x][t], dp[x-1][t-1])
            if x != 4:
                dp[x][t] = max(dp[x][t], dp[x+1][t-1])
        dp[X[t]][t] += A[t]
    print(max(dp[x][max_t] for x in range(5)))


if __name__ == "__main__":
    main()
