N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]

l_min = 0
r_min = N
for g in G:
    l_min = max(l_min, g[0])
    r_min = min(r_min, g[1])
print(max(0, r_min - l_min + 1))
