import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); a = int(data[idx + 1]); b = int(data[idx + 2])
        idx += 3

        blue_centered = (n % 2) == (b % 2)

        if a <= b:
            out.append("YES" if blue_centered else "NO")
        else:
            red_centered = (n % 2) == (a % 2)
            out.append("YES" if (blue_centered and red_centered) else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# Time Complexity: O(t) (input reading dominates)
# Space Complexity: O(1) extra (excluding input storage)