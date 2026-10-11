# Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())

    """
    Key Observation:
    - If n % 3 == 0:
      First player cannot force n
      to become divisible by 3.
    - Otherwise:
      First player wins in one move.
    """

    if n % 3 == 0:
        print("Second")
    else:
        print("First")

"""
Time Complexity:
- O(t), where t is the number of test cases.

Space Complexity:
- O(1) extra space.
- O(t) input space for reading all inputs.
"""