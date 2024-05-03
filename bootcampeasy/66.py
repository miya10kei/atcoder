S = input()

n = S.count("N")
w = S.count("W")
s = S.count("S")
e = S.count("E")

ans = "Yes"
if (n == 0 and s != 0) or (n != 0 and s == 0):
    ans = "No"
if (w == 0 and e != 0) or (w != 0 and e == 0):
    ans = "No"
print(ans)
