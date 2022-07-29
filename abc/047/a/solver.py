abc = sorted(list(map(int, input().split())))
if abc[2] - abc[0] - abc[1] == 0:
    print("Yes")
else:
    print("No")
