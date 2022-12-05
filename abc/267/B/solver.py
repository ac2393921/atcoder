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
    s = si()

    def search(column):
        for i in range(7):
            for j in range(i):
                if column[i] and column[j]:
                    for k in range(j + 1, i):
                        if not column[k]:
                            return 'Yes'
        return 'No'

    s = '$' + s
    if s[1] == '1':
        print('No')
    else:
        column = [False] * 7
        column[0] = (s[7] == '1')
        column[1] = (s[4] == '1')
        column[2] = (s[2] == '1') or (s[8] == '1')
        column[3] = (s[1] == '1') or (s[5] == '1')
        column[4] = (s[3] == '1') or (s[9] == '1')
        column[5] = (s[6] == '1')
        column[6] = (s[10] == '1')
        print(search(column))


if __name__ == "__main__":
    main()
