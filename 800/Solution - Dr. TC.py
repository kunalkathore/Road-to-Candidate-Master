import sys
input = sys.stdin.readline

test_cases = int(input().strip())  # number of test cases

for _ in range(test_cases):
    n = int(input().strip())  # string length
    s = input().strip()       # binary string

    total_ones = 0

    # Each position contributes independently:
    # - if s[i] == '1' => contributes (n - 1)
    # - if s[i] == '0' => contributes 1
    for bit in s:
        if bit == '1':
            total_ones += (n - 1)
        else:
            total_ones += 1

    print(total_ones)

"""
Time Complexity: O(n) per test case
Space Complexity: O(n) per test case (including input string)
"""