import math

# Number of test cases
T = int(input())

for _ in range(T):
    n = int(input())

    # Fix c = 1
    # Try small values of b until gcd(a, b) == 1
    b = 2
    while True:
        a = n - 1 - b
        if math.gcd(a, b) == 1:
            print(a, b, 1)
            break
        b += 1

"""
Time Complexity:
- GCD computation: O(log n)
- Only a few iterations per test case
- Per test case: O(1) (amortized)
- Overall: O(T)

Space Complexity:
- O(1) extra space
"""