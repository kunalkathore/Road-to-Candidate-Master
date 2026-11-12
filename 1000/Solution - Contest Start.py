import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    k = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(k):
        n = int(data[idx]); x = int(data[idx + 1]); t = int(data[idx + 2])
        idx += 3

        d = t // x

        if d >= n:
            ans = n * (n - 1) // 2
        else:
            ans = (n - d) * d + d * (d - 1) // 2

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

# Time Complexity: O(k) total (O(1) per test case) 
# Space Complexity: O(1) extra space