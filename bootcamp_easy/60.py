N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    sum = 0
    for j in range(N):
        if PX[i][0] == j + 1:
            sum += PX[i][1]
        else:
            sum += T[j]
    print(sum)
