import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    # Build prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    total_sum = prefix[n]

    for _ in range(q):
        l, r, k = map(int, input().split())

        old_segment_sum = prefix[r] - prefix[l - 1]
        new_segment_sum = k * (r - l + 1)

        new_total = total_sum - old_segment_sum + new_segment_sum

        if new_total % 2 == 1:
            print("YES")
        else:
            print("NO")

"""
Time Complexity:
- Prefix sum computation: O(n)
- Each query: O(1)
- Total per test case: O(n + q)

Space Complexity:
- Prefix array: O(n)
"""