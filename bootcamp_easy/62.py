H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for i in range(H * 2):
    index = int((i + 1 + 1) / 2) - 1
    t = []
    for j in range(W):
        t.append(C[index][j])
    print("".join(t))
