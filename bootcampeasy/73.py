N = int(input())
n = str(N)


ans = 0
if len(n) == 1:
    ans = N
else:
    if n[1:].count("9") == len(n) - 1:
        ans = int(n[0]) + (9 * (len(n) - 1))
    else:
        ans = (int(n[0]) - 1) + (9 * (len(n) - 1))
print(ans)
