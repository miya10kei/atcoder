A, B = map(int, input().split())


def is_palindromic(s):
    x = str(s)
    for j in range(int(len(x) / 2)):
        if x[j] != x[-j - 1]:
            return False
    return True


cnt = 0
for i in range(A, B + 1):
    cnt += 1 if is_palindromic(i) else 0
print(cnt)
