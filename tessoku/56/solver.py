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
    N, Q = im()
    S = si()
    q = irl(Q)

    B = [1] * (N+1)
    for i in range(N):
        B[i+1] = (B[i]*100) % MOD

    H = [None]*(N+1)
    H[0] = 0
    for i in range(N):
        H[i+1] = (H[i]*100 + ord(S[i])) % MOD

    for a, b, c, d in q:
        ab = (H[b] - (B[b-a+1]*H[a-1])) % MOD
        cd = (H[d] - (B[d-c+1]*H[c-1])) % MOD

        if ab == cd:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
