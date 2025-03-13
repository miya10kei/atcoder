A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

s = [[False] * 3 for _ in range(3)]
for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                s[i][j] = True

# 横
for i in range(3):
    if all(s[i]):
        print("Yes")
        exit(0)

# 縦
for i in range(3):
    if all([s[j][i] for j in range(3)]):
        print("Yes")
        exit(0)

# 斜め
if s[1][1]:
    if (s[0][2] and s[2][0]) or (s[0][0] and s[2][2]):
        print("Yes")
        exit(0)
print("No")
