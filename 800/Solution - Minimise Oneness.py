import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out = []
    idx = 1

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        # Optimal construction: one '1', remaining (n-1) are '0'
        out.append('1' + '0' * (n - 1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# Time Complexity: O(n) per test case
# Space Complexity: O(1) per test case, since no extra space is used