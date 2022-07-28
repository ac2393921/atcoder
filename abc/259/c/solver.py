S = input()
T = input()

s = []
cnt = 0
tmp = ""
for i in range(len(S)):
    cnt += 1
    if i != len(S) - 1:
        if S[i] != S[i + 1]:
            s.append([S[i], cnt])
            cnt = 0
    else:
        s.append([S[i], cnt])
        cnt = 0

t = []
cnt = 0
tmp = ""
for i in range(len(T)):
    cnt += 1
    if i != len(T) - 1:
        if T[i] != T[i + 1]:
            t.append([T[i], cnt])
            cnt = 0
    else:
        t.append([T[i], cnt])
        cnt = 0

if len(s) != len(t):
    print("No")
    exit()

for i in range(len(s)):
    if s[i][0] != t[i][0] or (s[i][1] == 1 and s[i][1] < t[i][1]) or s[i][1] > t[i][1]:
        print("No")
        exit()
print("Yes")
