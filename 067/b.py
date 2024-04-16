N, K = (int(x) for x in input().split())

l = list(int(x) for x in input().split())

sum = 0
list.sort(l, reverse=True)

for i in range(0, K):
    sum += l[i]
print(sum)
