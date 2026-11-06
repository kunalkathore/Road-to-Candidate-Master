t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 1:   # Impossible case
        print(-1)
        continue

    took = [False] * (n + 1)  # Track used numbers
    q = []

    # Greedy fill positions 0 to n-3
    for i in range(n - 2):
        k = 1
        while took[k] or k == p[i]:
            k += 1
        q.append(k)
        took[k] = True

    # Handle last two positions
    a = b = -1
    for i in range(1, n + 1):
        if not took[i]:
            if a == -1:
                a = i
            else:
                b = i

    if a != p[n-2] and b != p[n-1]:
        q.extend([a, b])
    else:
        q.extend([b, a])

    print(*q)

"""
Time Complexity:
- O(n^2) per test case (due to scanning for smallest unused number)
- Overall O(sum of n^2), acceptable for n <= 1000

Space Complexity:
- O(n) for arrays p, q, and took
"""