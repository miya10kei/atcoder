S = input()

d = "abcdefghijklmnopqrstuvwxyz"

for s in S:
    d = d.replace(s, "")
if len(d) == 0:
    print("None")
else:
    print(d[0])
