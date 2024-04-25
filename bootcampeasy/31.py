S = input()
S = "".join(sorted(S))

for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        print("no")
        exit(0)
print("yes")
