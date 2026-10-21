t = int(input())

for _ in range(t):
    X, Y, K = map(int, input().split())  # Read input
    M = min(X, Y)  # Maximum square size that fits in the rectangle

    # Segment AB: (0,0) -> (M,M)
    print(0, 0, M, M)

    # Segment CD: (0,M) -> (M,0)
    print(0, M, M, 0)

"""
Time Complexity:
- O(1) per test case
- Overall: O(t)

Space Complexity:
- O(1) extra space
"""