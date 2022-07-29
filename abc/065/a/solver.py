X, A, B = map(int, input().split())
E = B - A
if E <= 0:
    print("delicious")
elif E <= X:
    print("safe")
else:
    print("dangerous")
