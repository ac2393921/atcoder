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

    odd = []
    even = []
    for a in sorted(A, reverse=True):
        if a % 2 == 0:
            odd.append(a)
        else:
            even.append(a)

    if len(odd) <= 1 and len(even) <= 1:
        print(-1)
        exit()

    if len(odd) <= 1:
        print(even[0]+even[1])
    elif len(even) <= 1:
        print(odd[0]+odd[1])
    else:
        print(max(odd[0]+odd[1], even[0]+even[1]))


if __name__ == "__main__":
    main()
