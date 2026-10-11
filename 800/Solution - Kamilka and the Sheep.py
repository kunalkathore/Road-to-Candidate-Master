def solve():
    n = int(input())                  # Number of sheep
    a = list(map(int, input().split()))  # Beauty levels
 
    # Sort to get minimum and maximum values
    a.sort()
 
    # Maximum pleasure is max(a) - min(a)
    print(a[-1] - a[0])
 
 
t = int(input())                      # Number of test cases
for _ in range(t):
    solve()

"""
Time Complexity:
- Reading input: O(n)
- Sorting the array: O(n log n)
- Output operation: O(1)
- Per test case: O(n log n)

Space Complexity:
- O(n) for storing the array
- Python's sort is in-place (Timsort), so no extra significant space is used
"""