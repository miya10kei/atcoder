N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

m = {}
for i in range(M):
    m[A[i][0]] = m.get(A[i][0], 0) + 1
    m[A[i][1]] = m.get(A[i][1], 0) + 1
for i in range(N):
    print(m.get(i + 1, 0))
