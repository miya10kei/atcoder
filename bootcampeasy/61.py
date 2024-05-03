S = input()
T = input()

ans = "No"

for i in range(len(S)):
    if (S := f"{S[-1]}{S[0:-1]}") == T:
        ans = "Yes"
        break
print(ans)
