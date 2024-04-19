N, A, B = map(int, input().split())
S = input()

passed = b_passed = 0
for s in S:
    if s == "a":
        if passed < A + B:
            passed += 1
            print("Yes")
            continue
    elif s == "b":
        if passed < A + B and b_passed < B:
            passed += 1
            b_passed += 1
            print("Yes")
            continue
    print("No")
