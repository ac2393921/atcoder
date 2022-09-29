H, W = map(int, input().split())
G = [[""] * (W + 1)] + [[""] + list(input()) for _ in range(H)]

i, j = 1, 1
count = 0

while H * W + 1:
    if i != 1 and G[i][j] == "U":
        G[i][j] = ""
        i -= 1
    elif i != H and G[i][j] == "D":
        G[i][j] = ""
        i += 1
    elif j != 1 and G[i][j] == "L":
        G[i][j] = ""
        j -= 1
    elif j != W and G[i][j] == "R":
        G[i][j] = ""
        j += 1
    elif not G[i][j]:
        break
    else:
        print(i, j)
        exit()

    count += 1
print(-1)
