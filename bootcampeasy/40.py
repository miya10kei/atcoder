a, b = map(int, input().split())

if a == 0 or b == 0:
    print("Zero")
elif a < 0 and 0 < b:
    print("Zero")
elif 0 < a and 0 < b:
    print("Positive")
else:
    if (abs(b - a) + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")
