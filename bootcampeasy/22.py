N, x = map(int, input().split())
A = list(map(int, input().split()))

if x == sum(A):
    print(N)
    exit(0)

A.sort()
ans = 0
s = 0
for i in range(N - 1):
    s += A[i]
    ans += 1
    if s > x:
        ans -= 1
print(ans)
