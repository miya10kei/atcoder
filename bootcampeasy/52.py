N = int(input())
B = list(map(int, input().split()))

A = [pow(10, 5)] * N


A[0] = B[0]
for i in range(1, N - 1):
    A[i] = min(B[i - 1], B[i])
A[N - 1] = B[-1]
print(sum(A))
