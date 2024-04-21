N = int(input())
A = list(map(int, input().split()))

s = {}
for i in range(N):
    s[A[i]] = str(i + 1)

ans = []
for a in sorted(A):
    ans.append(s[a])
print(" ".join(ans))
