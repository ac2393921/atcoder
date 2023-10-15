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


sys.setrecursionlimit(11 ** 6)
INF = float('inf')
MOD = 11 ** 9 + 7


def main():
    N = ii()
    ans = []
    for i in range(2 ** N):
        score = 0
        tmp = ""
        for j in range(N):
            if ((i >> j) & 1):
                tmp += "("
                score += 1
            else:
                tmp += ")"
                score -= 1

            if score < 0:
                break
        if score == 0:
            ans.append(tmp)

    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
