t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())      # length of encrypted string
    s = input()           # encrypted string

    i = 0
    result = []

    # Traverse the encrypted string
    while i < n:
        start = i                 # start of current block
        result.append(s[i])       # original character
        i += 1

        # Move forward until the same character appears again
        while s[i] != s[start]:
            i += 1
        i += 1                    # skip the matching character

    print("".join(result))

"""
Time Complexity:
- Reading input: O(n) per test case
- Traversing the encrypted string: O(n)
- Per test case: O(n)
- Overall: O(sum of n over all test cases)

Space Complexity:
- O(1) extra space (only index variables are used)
"""