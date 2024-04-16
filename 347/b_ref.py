S = input()
ans = set()
for i in range(len(S)):
    for j in range(1, len(S) - i + 1):
        ans.add(S[i : (i + j)])
print(len(ans))
