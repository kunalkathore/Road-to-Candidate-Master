t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))

    current = 0  # length of current valid segment
    answer = 0

    for x in arr:
        if x <= q:
            current += 1
        else:
            if current >= k:
                length = current - k + 1
                answer += length * (length + 1) // 2
            current = 0

    # handle last segment
    if current >= k:
        length = current - k + 1
        answer += length * (length + 1) // 2

    print(answer)

"""
Time Complexity:  O(n) per test case — single pass including input.
Space Complexity: O(n) for input reading and O(1) for extra space beyond input storage.
"""