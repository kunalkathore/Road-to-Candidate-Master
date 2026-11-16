def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Compressed array to remove consecutive duplicates
    compressed = []

    for x in arr:
        if not compressed or compressed[-1] != x:
            compressed.append(x)

    num_valley = 0
    m = len(compressed)

    # Count valley positions (local minima)
    for i in range(m):
        left_ok = (i == 0 or compressed[i - 1] > compressed[i])
        right_ok = (i == m - 1 or compressed[i] < compressed[i + 1])

        if left_ok and right_ok:
            num_valley += 1

    # Exactly one valley required
    print("YES" if num_valley == 1 else "NO")


t = int(input())
for _ in range(t):
    solve()

"""
Time Complexity: O(n) per test case
Space Complexity: O(n) for compressed array
"""