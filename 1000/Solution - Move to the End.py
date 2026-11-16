import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # pmax[i] = maximum among first i elements
    # psum[i] = sum of first i elements
    pmax = [0] * (n + 1)
    psum = [0] * (n + 1)

    for i in range(n):
        pmax[i + 1] = max(pmax[i], a[i])
        psum[i + 1] = psum[i] + a[i]

    result = []
    for k in range(1, n + 1):
        suffix_sum = psum[n] - psum[n - k + 1]
        best_prefix = pmax[n - k + 1]
        result.append(str(best_prefix + suffix_sum))

    print(" ".join(result))

"""
Time Complexity:  O(n) per test case — prefix computation + loop
Space Complexity: O(n) — input list + prefix arrays
"""