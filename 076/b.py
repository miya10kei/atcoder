N = int(input())
K = int(input())

num = 1
for i in range(N):
    a = num * 2
    b = num + K
    num = a if a < b else b
print(num)
