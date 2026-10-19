t = int(input())

for _ in range(t):
    n = int(input())
    answer = 0

    # Check divisibility starting from 1
    for i in range(1, 101):
        if n % i == 0:
            answer = i
        else:
            break

    print(answer)

"""
Time Complexity:
O(1) per test case (loop runs at most ~50 iterations))

Space Complexity:
O(1)
"""