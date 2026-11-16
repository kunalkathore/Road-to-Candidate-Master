def solve():
    n = int(input())  # Number of fields
    a = list(map(int, input().split()))

    p = [[], []]  # p[0] = even, p[1] = odd
    for x in a:
        p[x % 2].append(x)

    ans = 0
    if p[1]:  # If at least one odd, add all even fields
        ans += sum(p[0])

    p[1].sort(reverse=True)  # Sort odd fields descending
    m = len(p[1])
    for i in range((m + 1) // 2):  # Take half of largest odd fields
        ans += p[1][i]

    print(ans)

t = int(input())
for _ in range(t):
    solve()

# Time Complexity: O(n log n)
# Space Complexity: O(n)