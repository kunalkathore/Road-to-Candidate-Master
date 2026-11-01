t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = [0] * (k + 1)

    for x in arr:
        if x <= k:
            freq[x] += 1

    score = 0

    for x in range(1, k):
        if x < k - x:
            score += min(freq[x], freq[k - x])

    if k % 2 == 0:
        score += freq[k // 2] // 2

    print(score)

# Time Complexity: O(n)
# Space Complexity: O(n)