s = int(input())


def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)


a = [s]
i = 1
while True:
    y = f(a[i - 1])
    if y in a:
        print(i + 1)
        break
    a.append(y)
    i += 1
