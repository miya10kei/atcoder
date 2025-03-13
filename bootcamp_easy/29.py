S = input()

ans = 9999
for i in range(len(S) - 1):
    ans = min(ans, abs(753 - int(S[i : (i + 3)])))
print(ans)
