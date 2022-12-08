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
    def dfs(x, y, ans, n=1):
        G[x][y] = 1
        if n >= N:
            return int(ans)

        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]

        max_a = 0
        max_nx, max_ny = 0, 0
        for i in range(8):
            nx = (x + dx[i]) % N
            ny = (y + dy[i]) % N

            if G[nx][ny]:
                continue

            if max_a < int(A[nx][ny]):
                max_a = int(A[nx][ny])
                max_nx = nx
                max_ny = ny

        ans += A[max_nx][max_ny]
        return dfs(max_nx, max_ny, ans, n+1)

    N = ii()
    A = srl(N)

    ans = 0
    for d in range(8):
        for i in range(N):
            for j in range(N):
                G = [[0] * N for i in range(N)]
                a = dfs(i, j, A[i][j])
                ans = max(ans, a)

    print(ans)


if __name__ == "__main__":
    main()
