N = int(input())
SP = [list(input().split() + [i + 1]) for i in range(N)]

ans = sorted(SP, key=lambda x: int(x[1]), reverse=True)
ans = sorted(ans, key=lambda x: x[0])

for a in ans:
    print(a[2])
