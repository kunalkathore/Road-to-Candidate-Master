t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Pair and sort by a
    pairs = sorted(zip(a, b))

    # Print reordered a
    print(*[x[0] for x in pairs])

    # Print reordered b
    print(*[x[1] for x in pairs])

"""
Time Complexity: O(n log n) per test case
Space Complexity: O(n) including input arrays
"""