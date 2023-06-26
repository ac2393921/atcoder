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
    def check(n):
        num = 0  # 何個切れたか
        pre = 0  # 前回の切れ目

        # 貪欲法
        for i in range(N):
            # 切れ目が指定の数より大きければnumを1増加
            if A[i] - pre >= n:
                num += 1
                pre = A[i]

        # 最後のピースが指定より大きければ増加
        if L - pre >= n:
            num += 1

        # 切った全てがn以上であればTrue
        return (num >= K + 1)

    N, L = im()
    K = ii()
    A = il()

    # 二分探索
    l, r = -1, L+1
    while r - l > 1:
        mid = (l+r)//2

        # 全て切れれば右にずらす
        if check(mid):
            l = mid
        else:
            r = mid

    print(l)


if __name__ == "__main__":
    main()
