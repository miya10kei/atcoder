A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(M)]

ans = [min(a) + min(b)]
for k in range(M):
    ans.append(a[m[k][0] - 1] + b[m[k][1] - 1] - m[k][2])
print(min(ans))
