N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

words = set(s).union(set(t))
answer = max(0, *[s.count(word) - t.count(word) for word in words])

print(answer)
