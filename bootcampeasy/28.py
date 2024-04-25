N = int(input())
A = list(map(int, input().split()))

ans = 0
loop = True
while loop:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i] / 2
        else:
            loop = False
            break
    if loop:
        ans += 1
print(ans)
