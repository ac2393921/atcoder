a, b, c, d = map(int, input().split())

if (a - b <= d and b - c <= d) or (a - c <= d):
    print("Yes")
else:
    print("No")
