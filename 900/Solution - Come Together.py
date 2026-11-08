def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

t = int(input())
for _ in range(t):
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))
    
    # Apply derived formula
    ans = (dist(A, B) + dist(A, C) - dist(B, C)) // 2 + 1
    print(ans)

"""
Time Complexity: O(1) per test case
Space Complexity: O(1)
"""