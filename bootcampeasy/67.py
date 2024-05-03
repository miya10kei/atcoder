N = int(input())
S = [input() for _ in range(N)]

m = {}
for i in range(N):
    m[S[i]] = m.get(S[i], 0) + 1
mv = max(m.values())
ans = []
for k, v in m.items():
    if v == mv:
        ans.append(k)

for a in sorted(ans):
    print(a)
