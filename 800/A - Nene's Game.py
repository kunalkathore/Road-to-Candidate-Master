# We only need the smallest value a[0]
# Winners = min(n, a[0] - 1)

def solve():
    k, q = map(int, input().split())
    
    # Read array a
    a = list(map(int, input().split()))
    
    # Process each query
    n_values = list(map(int, input().split()))
    for n in n_values:
        print(min(a[0] - 1, n), end=" ")
    print()


t = int(input())
for _ in range(t):
    solve()

"""
Time Complexity:
- Per test case: O(k + q)
- Overall: O(t * (k + q))

Space Complexity:
- O(k) for storing array a
"""