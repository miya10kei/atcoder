X = list(map(int, input().split()))
X.sort()

min = X[0]
median = X[1]
max = X[2]


answer = max - median
t = max - (min + answer)

if t % 2 == 0:
    answer += int(t / 2)
else:
    answer += int(t / 2)
    answer += int(t % 2) * 2

print(answer)
