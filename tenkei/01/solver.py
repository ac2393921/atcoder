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
    def judge(mid):
        tmp = 0
        cnt = 0

        for i in range(N):
            # 羊羹の長さが指定の長さ(mid)より大きいか、
            # 残りの羊羹の長さが指定の長さより大きいかを判定
            if A[i] - tmp >= mid and L - A[i] >= mid:
                cnt += 1
                tmp = A[i]

        # 切った数がK以上に切り分けられればTrue
        if cnt >= K:
            return True
        else:
            return False

    N, L = im()
    K = ii()
    A = il()

    right = L
    left = 0

    while right - left > 1:
        mid = (left + right) // 2

        # 切り分けられた場合、最大化するために左端を大きくする
        if judge(mid):
            left = mid
        # 切り分けられなかった場合、条件を小さくするために右端を小さくする
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
