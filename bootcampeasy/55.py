import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        d = 0
        for k in range(D):
            d += pow(X[i][k] - X[j][k], 2)
        t = math.sqrt(d)
        ans += 1 if t.is_integer() else 0
print(ans)
