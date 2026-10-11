t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Required number of special characters

    # Odd number of special characters is impossible
    if n % 2 == 1:
        print("NO")
        continue

    print("YES")

    # Build the string using n/2 blocks of length 2
    # Alternate characters to avoid merging blocks
    result = []
    for i in range(n // 2):
        ch = 'A' if i % 2 == 0 else 'B'
        result.append(ch * 2)

    print("".join(result))

"""
Time Complexity:
- Reading input: O(1) per test case
- Constructing the string: O(n)
- Per test case: O(n)
- Overall: O(sum of n over all test cases)

Space Complexity:
- O(1) extra space (output string is not counted as extra memory)
"""