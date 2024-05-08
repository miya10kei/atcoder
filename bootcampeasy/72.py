X = int(input())


def max_pow(b):
    ret = 0
    for p in range(2, X + 1):
        if (t := pow(b, p)) <= X:
            ret = t
        else:
            return ret


ans = 0
if X == 1:
    ans = 1
else:
    for b in range(2, X + 1):
        if (t := max_pow(b)) <= X:
            if ans <= t:
                ans = t
print(ans)
