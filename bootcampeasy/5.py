N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for a in A:
    s = 0
    for i in range(M):
        s += a[i] * B[i]
    if s + C > 0:
        cnt += 1
print(cnt)
