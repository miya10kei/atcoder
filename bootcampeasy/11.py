N = int(input())

ans = -1
cnt = -1
for i in range(1, N + 1):
    x = i
    j = 0
    while x % 2 == 0:
        j += 1
        x /= 2
    if j > cnt:
        ans = i
        cnt = j
print(ans)
