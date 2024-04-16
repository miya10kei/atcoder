S = input()
T = input()

start = 0
if T.endswith("X"):
    T = T[0:2]
    finds = [False] * 2
else:
    finds = [False] * 3
for i, t in enumerate(T):
    for j in range(start, len(S)):
        if S[j] == t.lower():
            finds[i] = True
            start = j + 1
            break
print("Yes" if all(finds) else "No")
