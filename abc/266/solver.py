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


def is_cw(x1, y1, x2, y2, x3, y3):
    vec1 = [x1-x2, y1-y2]
    vec2 = [x3-x2, y3-y2]

    return vec1[0] * vec2[1] - vec1[1] * vec2[0] < 0


def main():
    Ax, Ay = im()
    Bx, By = im()
    Cx, Cy = im()
    Dx, Dy = im()

    if is_cw(Ax, Ay, Bx, By, Cx, Cy) and is_cw(Bx, By, Cx, Cy, Dx, Dy) and is_cw(Cx, Cy, Dx, Dy, Ax, Ay) and is_cw(Dx, Dy, Ax, Ay, Bx, By):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
