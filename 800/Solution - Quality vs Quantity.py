import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n

        a.sort()

        # k = floor((n - 1) / 2) ensures Blue has (k+1) elements and Red has k elements
        k = (n - 1) // 2

        blue_sum = sum(a[:k+1])     # smallest (k+1)
        red_sum = sum(a[n-k:])      # largest k

        out.append("YES" if red_sum > blue_sum else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

"""
Time Complexity: O(n log n) per test case (sorting dominates).
Space Complexity: O(n) for storing the array and input tokens.
"""