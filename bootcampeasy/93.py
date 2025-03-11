import sys

N = int(input())
A = list(map(int, input().split()))

length = sum(A)
left = 0
answer = sys.maxsize

for a in A:
    left += a
    answer = min(answer, abs(left - (length - left)))

print(answer)
