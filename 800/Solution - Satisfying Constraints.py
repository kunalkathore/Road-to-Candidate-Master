def solve():
    n = int(input())

    # l = minimum possible value of k
    # r = maximum possible value of k
    l, r = 1, 10**9

    # Store values where k != x
    not_equal = []

    for _ in range(n):
        a, x = map(int, input().split())

        # Type 1: k >= x
        # Take maximum to satisfy all such constraints
        if a == 1:
            l = max(l, x)

        # Type 2: k <= x
        # Take minimum to satisfy all such constraints
        elif a == 2:
            r = min(r, x)

        # Type 3: k != x
        # Store forbidden values
        else:
            not_equal.append(x)

    # Count forbidden values inside [l, r]
    blocked = 0
    for x in not_equal:
        if l <= x <= r:
            blocked += 1

    # Total valid values
    print(max(r - l + 1 - blocked, 0))


t = int(input())
for _ in range(t):
    solve()

"""
Time Complexity:
- Reading input constraints: O(n)
- Processing type-1 and type-2 constraints: O(n)
- Checking forbidden values (type-3): O(n)
- Per test case: O(n)
- Overall: O(sum of n over all test cases)

Space Complexity:
- O(n) extra space for storing forbidden (not equal) values
"""