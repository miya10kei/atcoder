S = input()
K = int(input())

index = -1
t = ""
for i in range(len(S)):
    if S[i] == "1":
        index = i + 1
    else:
        t = S[i]
        break
print(1 if index >= K else t)
