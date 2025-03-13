N = int(input())
W = [input() for _ in range(N)]

words = [W[0]]
for i in range(1, N):
    if W[i] in words or W[i][0] != words[-1][-1]:
        print("No")
        exit(0)
    words.append(W[i])
print("Yes")
