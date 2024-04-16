N = int(input())
AC = [list(map(int, input().split())) for _ in range(N)]

m = {}
for ac in AC:
    if ac[0] < m.get(ac[1], pow(10, 9)):
        m[ac[1]] = ac[0]

print(max(m.values()))
