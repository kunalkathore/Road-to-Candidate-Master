q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()

    n, m = len(s), len(t)
    lcp = 0

    # Find longest common prefix
    while lcp < n and lcp < m and s[lcp] == t[lcp]:
        lcp += 1

    # Case 1: type everything
    ans = n + m

    # Case 2: use one copy
    if lcp > 0:
        ans = min(ans, n + m - lcp + 1)

    print(ans)

# Time Complexity: O(min(n, m)) per test case
# Space Complexity: O(1)