S = input()

cnt = 0
prev = ""
i = 0
while i < len(S):
    for j in range(i + 1, len(S) + 1):
        if S[i:j] != prev:
            prev = S[i:j]
            cnt += 1
            i = j
            break
        if j == len(S):
            i = j
print(cnt)
