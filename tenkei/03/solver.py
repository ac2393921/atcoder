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
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = im()
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    def dfs(s):
        dist = [-1] * N
        dist[s] = 0
        st = [s]

        # スタックによるDFS
        while st:
            v = st.pop()
            for nv in G[v]:
                # まだ探索していなければ
                if dist[nv] == -1:
                    st.append(nv)
                    dist[nv] = dist[v] + 1

        return dist

    dist0 = dfs(0)
    # 最短距離が最大になるポイントを取得
    mv = max(enumerate(dist0), key=lambda x: x[1])[0]
    distmv = dfs(mv)
    print(max(distmv)+1)


if __name__ == "__main__":
    main()
