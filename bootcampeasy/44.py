S = input()

cnt1 = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] != "1":
            cnt1 += 1
    else:
        if S[i] != "0":
            cnt1 += 1

cnt2 = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] != "0":
            cnt2 += 1
    else:
        if S[i] != "1":
            cnt2 += 1
print(min(cnt1, cnt2))
