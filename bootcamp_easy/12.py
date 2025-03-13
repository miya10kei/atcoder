K, N = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
s = []
for i in range(N):
    if i <= N - 2:
        s.append(A[i + 1] - A[i])
    else:
        s.append(K - A[i] + A[0])
print(K - max(s))
