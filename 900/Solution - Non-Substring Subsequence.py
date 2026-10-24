t = int(input("Enter number of test cases: "))

for _ in range(t):
    n, q = map(int, input().split())
    s = input()

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1  # convert to 0-based indexing

        bad = True  # assume no good subsequence

        # Check before l
        for i in range(l):
            if s[i] == s[l]:
                bad = False
                break

        # Check after r
        if bad:
            for i in range(r + 1, n):
                if s[i] == s[r]:
                    bad = False
                    break

        print("NO" if bad else "YES")

"""
Time Complexity:
- For each query: O(n)
- For each test case: O(n * q)

Space Complexity:
- O(1) extra space
"""