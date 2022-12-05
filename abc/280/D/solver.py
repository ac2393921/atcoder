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
    def f(n, p):
        if n == 0:
            return 0
        n //= p
        return n+f(n, p)

    K = ii()
    ps = defaultdict(int)

    x = K
    for i in range(2, math.floor(K**0.5)+1):
        if x % i:
            continue
        cnt = 0
        while x % i == 0:
            x //= i
            cnt += 1
        ps[i] = cnt
    if x != 1:
        ps[K] = 1

    ac, wa = K, 0
    while ac-wa > 1:
        wj = (ac+wa)//2
        ok = True

        for p, cnt in ps.items():
            if f(wj, p) < cnt:
                ok = False
        if ok:
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == "__main__":
    main()
