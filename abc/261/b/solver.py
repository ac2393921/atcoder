N = int(input())
A = list(input() for _ in range(N))
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if A[i][j] == "D" and A[j][i] != "D" or A[i][j] != "D" and A[j][i] == "D":
            print("incorrect")
            exit()

        if A[i][j] == A[j][i] != "D":
            print("incorrect")
            exit()
print("correct")
