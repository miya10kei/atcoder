N, L = map(int, input().split())
S = [input() for _ in range(N)]
ans = "".join(sorted(S))
print(ans)
