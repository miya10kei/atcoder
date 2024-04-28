A, B = map(int, input().split())
S = input()

ans = "No"

if len(S) == A + B + 1:
    for i in range(len(S)):
        if i == A:
            if S[i] == "-":
                ans = "Yes"
            else:
                ans = "No"
        else:
            if "0" <= S[i] and S[i] <= "9":
                ans = "Yes"
            else:
                ans = "No"
        if ans == "No":
            break
print(ans)
