S = input()

ans = set()
t = ""
for i in range(len(S)):
    t = S[i]
    ans.add(t)
    for k in range(i + 1, len(S)):
        t = f"{t}{S[k]}"
        ans.add(t)
print(len(ans))
