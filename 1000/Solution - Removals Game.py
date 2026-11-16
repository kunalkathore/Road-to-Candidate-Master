import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a == b:
        print("Bob")
        continue

    if a[::-1] == b:
        print("Bob")
        continue

    print("Alice")

"""
--------------------------------------------------
Time and Space Complexity Analysis
--------------------------------------------------
- Time Complexity:
  O(n) per test case (list comparison + reverse)
  Total: O(sum of n) ≤ 3 × 10^5

- Space Complexity:
  O(n) for storing the two permutations
--------------------------------------------------
"""