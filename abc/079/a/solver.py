N = input()
tmp = N[0]
cnt = 1
for i in range(1, 4):
    cnt += 1

    if N[i] == tmp:
        if cnt == 3:
            print("Yes")
            exit()
    else:
        cnt = 1
    tmp = N[i]
print("No")
