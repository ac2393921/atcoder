RC = [
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
    ["1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "1", "1", "1", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "1", "1", "1", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
]
R, C = map(int, input().split())
if RC[R - 1][C - 1] == "1":
    print("black")
else:
    print("white")