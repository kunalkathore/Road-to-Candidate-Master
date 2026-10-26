import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1

        # Frequency array for values 1..n
        freq = [0] * (n + 1)
        for _ in range(n):
            x = data[idx]
            idx += 1
            freq[x] += 1

        # If any value occurs odd times -> Alice wins
        has_odd = any((freq[v] & 1) == 1 for v in range(1, n + 1))
        out.append("YES" if has_odd else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

"""
Time Complexity: O(n) per test case
Space Complexity: O(n)
"""