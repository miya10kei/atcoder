W = input()

M = {}
for w in W:
    M[w] = M.get(w, 0) + 1
for v in M.values():
    if v % 2 != 0:
        print("No")
        exit(0)
print("Yes")
