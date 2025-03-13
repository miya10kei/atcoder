N, M = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(N)]

M = {}
for i in range(N):
    for j in range(1, K[i][0] + 1):
        M[K[i][j]] = M.get(K[i][j], 0) + 1

cnt = 0
for v in M.values():
    cnt += 1 if v == N else 0
print(cnt)
