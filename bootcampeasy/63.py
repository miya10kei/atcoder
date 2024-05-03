N = int(input())
a = list(map(int, input().split()))

ans = 0
next = 1
for i in range(N):
    if a[i] == next:
        next += 1
    else:
        ans += 1
print(ans if next > 1 else -1)
