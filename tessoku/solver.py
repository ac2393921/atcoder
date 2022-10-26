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
    N, X, Y = im()
    A = il()
    A_max = max(A)
    min_xy = min(X, Y)

    grundy = [0] * 1000001
    for i in range(100001):
        t = [0]*3
        if i - X >= 0:
            t[grundy[i-X]] = 1
        if i - Y >= 0:
            t[grundy[i-Y]] = 1
        if not t[0]:
            grundy[i] = 0
        elif not t[1]:
            grundy[i] = 1
        else:
            grundy[i] = 2

    xor_sum = 0
    for i in range(N):
        xor_sum = xor_sum ^ grundy[A[i]]
    print("First" if xor_sum else "Second")


if __name__ == "__main__":

    main()
