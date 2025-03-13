A, B, K = map(int, input().split())

n = B - A + 1
if n <= K * 2:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, A + K):
        print(i)
    for i in range(A + n - K, A + n):
        print(i)
