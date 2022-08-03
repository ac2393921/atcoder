import math


def solve(t):
    theta = 2 * math.pi * t / T
    h = L / 2 - L / 2 * math.cos(theta)
    y = -L / 2 * math.sin(theta)
    dist = (X ** 2 + (y - Y) ** 2) ** 0.5

    return math.atan(h / dist) / math.pi * 180


T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    E = int(input())
    print(solve(E))
