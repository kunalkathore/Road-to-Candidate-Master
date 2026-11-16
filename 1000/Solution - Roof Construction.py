import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []

    for _ in range(t):
        n = int(next(it))

        # m = highest power of two <= (n - 1)
        m = 1 << ((n - 1).bit_length() - 1)

        # Build the permutation
        perm = list(range(m - 1, -1, -1)) + list(range(m, n))
        out_lines.append(" ".join(map(str, perm)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

"""
Time Complexity:  O(n) per test case (creating + printing n numbers), overall O(sum n)
Space Complexity: O(n) per test case for the output line/list (input not stored)
"""