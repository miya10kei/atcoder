X = int(input())

m = X % 100
p = [5, 4, 3, 2, 1]

if m == 0:
    answer = 1
else:
    count = 0
    for i in p:
        while m > 0:
            if m - i >= 0:
                m -= i
                count += 1
            else:
                break
    answer = 1 if int(X / (count * 100)) > 0 else 0
print(answer)
