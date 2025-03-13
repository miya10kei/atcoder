N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split())) + [0]
ans = 0
for i in range(N + 1, -1, -1):
    ans += min(A[i], B[i] + B[i - 1])
    B[i - 1] = max(B[i - 1] - max(A[i] - B[i], 0), 0)
print(ans)
