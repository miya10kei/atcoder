N = int(input())

answer = 1
for i in range(1, N + 1):
    answer = (answer * i) % 1000000007

print(answer)
