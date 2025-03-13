N = int(input())
A = list(map(int, input().split()))

cnt = 0
min = 2 * pow(10, 5)
for i in range(N):
    if A[i] <= min:
        min = A[i]
        cnt += 1
print(cnt)
