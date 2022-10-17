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
    S = list(s_input())
    len_S = len(S)
    S = [""] + S
    T = list(s_input())
    len_T = len(T)
    T = [""] + T

    dp = [[0] * (len_T+1) for _ in range(len_S+1)]
    dp[0][0] = 0

    for i in range(len_S+1):
        for j in range(len_T+1):
            if S[i] and T[j] and S[i] == T[j]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            elif S[i] and T[j]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            elif T[j]:
                dp[i][j] = dp[i-1][j]
            elif S[i]:
                dp[i][j] = dp[i][j-1]

    print(dp[len_S][len_T])


if __name__ == "__main__":
    main()
