N = int(input())
a = list(map(int, input().split()))


def count_divisons_by_two(x):
    count = 0
    while x % 2 == 0:
        x /= 2
        count += 1
    return count


answer = sum([count_divisons_by_two(x) for x in a if x % 2 == 0])
print(answer)
