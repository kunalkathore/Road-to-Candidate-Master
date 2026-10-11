t = int(input())  # number of test cases

for _ in range(t):
    a, b, c, d = map(int, input().split())

    # Goals scored in second half
    c -= a
    d -= b

    # Make sure a <= b and c <= d
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c

    # Check the constraint for both halves
    if b <= 2 * a + 2 and d <= 2 * c + 2:
        print("YES")
    else:
        print("NO")

"""
Time Complexity:
- Reading input: O(1) per test case
- Arithmetic operations and comparisons: O(1)
- Per test case: O(1)
- Overall: O(T)

Space Complexity:
- O(1), only constant extra variables are used
"""