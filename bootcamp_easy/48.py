N = int(input())
M = list(map(int, input().split()))


m = 0
i = 0
while i < N - 1:
    cnt = 0
    for j in range(i, N - 1):
        i = j
        if M[j + 1] <= M[j]:
            cnt += 1
            m = max(m, cnt)
        else:
            break
    i += 1
print(m)
