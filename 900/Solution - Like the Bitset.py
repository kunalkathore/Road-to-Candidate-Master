def solve():
    n, k = map(int, input().split())
    s = input()

    # Step 1: Check for any block of consecutive '1's of length >= k
    # Two-pointer scan, each index visited once
    # Time Complexity: O(n)
    i = 0
    while i < n:
        if s[i] == '1':
            j = i
            while j < n and s[j] == '1':
                j += 1

            if j - i >= k:
                print("NO")
                return

            i = j
        else:
            i += 1

    print("YES")

    # Count number of '1's
    # Time Complexity: O(n)
    ones = s.count('1')

    # Step 3: Construct permutation
    # Single traversal of string
    # Time Complexity: O(n)
    small = 0
    large = ones
    ans = []

    for ch in s:
        if ch == '1':
            small += 1
            ans.append(small)
        else:
            large += 1
            ans.append(large)

    print(*ans)


t = int(input())
for _ in range(t):
    solve()


"""
==================== Complexity Analysis ====================

Time Complexity:
- O(n) per test case
- Overall O(Σn) ≤ O(2 × 10^5), where Σn is the sum of n over all test cases

Space Complexity:
- O(n) for storing the string and output permutation
- No extra auxiliary data structures used

=============================================================
"""