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
    N, M = im()
    G = defaultdict(list)
    for i in range(M):
        a, b, c = im()
        G[a].append((b, c))
        G[b].append((a, c))

    done = [0]*(N+1)
    cur = [20**9] * (N+1)

    T = []

    # スタート地点の初期化
    cur[1] = 0
    heappush(T, (cur[1], 1))

    # ダイクストラ法
    while T:
        # 最小値を取り出す
        _, pos = heappop(T)

        # 確定済みの場合スキップ
        if done[pos]:
            continue

        # 隣接する頂点(nex)のcurを計算
        done[pos] = True
        for i in range(len(G[pos])):
            nex, cost = G[pos][i]
            # すでに入力されている値より小さければ更新
            if cur[nex] > cur[pos] + cost:
                cur[nex] = cur[pos] + cost
                heappush(T, (cur[nex], nex))

    for i in range(1, N+1):
        if cur[i] == 20**9:
            print(-1)
        else:
            print(cur[i])


if __name__ == "__main__":
    main()
