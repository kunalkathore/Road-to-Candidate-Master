import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1

        a1 = int(data[idx]); a2 = int(data[idx + 1])
        idx += n  # skip the whole array (we already read first two)

        ans = a1 + min(a1, a2)
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# Time Complexity: O(sum n) because we read all input
# Space Complexity: O(1) extra (excluding input storage)