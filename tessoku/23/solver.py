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
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)


sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M = i_map()
    dp = [[INF]*(2**N) for _ in range(M+1)]
    dp[0][0] = 0
    T = [0] * (M+1)
    for i in range(1, M+1):
        A = s_list()
        T[i] = int(''.join(A), 2)

    for i in range(1, M+1):
        for s in range(1 << N):
            dp[i][s] = min(dp[i][s], dp[i-1][s])
            st = s | T[i]
            dp[i][st] = min(dp[i][st], dp[i-1][s] + 1)

    print(-1 if dp[-1][-1] == INF else dp[-1][-1])


if __name__ == "__main__":
    main()
