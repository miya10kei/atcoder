N = int(input())
a = map(int, input().split())

a = sorted(a)
a = a[N:]
ans = 0
for i in range(0, len(a), 2):
    ans += a[i]
print(ans)
