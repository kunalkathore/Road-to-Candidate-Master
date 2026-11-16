def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # pre[i]: minimum from a[0] to a[i]
    # suf[i]: maximum from a[i] to a[n-1]
    pre = [0] * n
    suf = [0] * n

    # Compute prefix minimums
    pre[0] = a[0]
    for i in range(1, n):
        pre[i] = min(pre[i - 1], a[i])

    # Compute suffix maximums
    suf[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        suf[i] = max(suf[i + 1], a[i])

    # Check condition for each index
    result = []
    for i in range(n):
        if a[i] == pre[i] or a[i] == suf[i]:
            result.append('1')
        else:
            result.append('0')

    print("".join(result))


t = int(input())
for _ in range(t):
    solve()

"""
Time Complexity:
- O(n) per test case

Space Complexity:
- O(n) for prefix and suffix arrays
"""