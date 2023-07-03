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
    H, W = im()
    A = irl(H)

    a1 = [sum(A[i]) for i in range(H)]

    a2 = []
    for i in range(W):
        tmp = 0
        for j in range(H):
            tmp += A[j][i]
        a2.append(tmp)

    ans = []
    for i in range(H):
        tmp = []
        for j in range(W):
            tmp.append(a1[i] + a2[j] - A[i][j])
        ans.append(tmp)

    for i in range(H):
        print(*ans[i])


if __name__ == "__main__":
    main()
