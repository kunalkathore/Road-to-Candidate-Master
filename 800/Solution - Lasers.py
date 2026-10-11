t = int(input())

for _ in range(t):
    n, m, x, y = map(int, input().split())

    # Read and ignore laser positions
    if n > 0:
        list(map(int, input().split()))
    if m > 0:
        list(map(int, input().split()))

    print(n + m)

"""
Time Complexity:
O(n + m) per test case
(input reading only)

Space Complexity:
O(1) extra space
(no extra storage required)
"""