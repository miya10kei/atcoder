import functools
import itertools
import operator

N = int(input())
A = list(map(int, input().split()))
A_plus = [x + 1 for x in A]
A_minus = [x - 1 for x in A]
answer = 0

z = list(zip(A, A_plus, A_minus))
for b in itertools.product(*z):
    product = functools.reduce(operator.mul, b, 1)
    answer += int(product % 2 == 0)
print(answer)
