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
    def score(a, b):
        cnt = 0
        for i in range(N):
            if a <= A[i] and A[i] <= a + K and b <= B[i] and B[i] <= b + K:
                cnt += 1
        return cnt

    N, K = im()
    A = []
    B = []
    for _ in range(N):
        a, b = im()
        A.append(a)
        B.append(b)

    ans = 0
    for a in range(1, 101):
        for b in range(1, 101):
            s = score(a, b)
            ans = max(ans, s)

    print(ans)


if __name__ == "__main__":
    main()
