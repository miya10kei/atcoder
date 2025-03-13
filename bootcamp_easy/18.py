S = input()

ans = 0
for i in range(len(S)):
    for j in range(1, len(S) + 1):
        t = S[i:j]
        if (
            len(t.replace("A", "").replace("C", "").replace("G", "").replace("T", ""))
            == 0
        ):
            if len(t) > ans:
                ans = len(t)
print(ans)
