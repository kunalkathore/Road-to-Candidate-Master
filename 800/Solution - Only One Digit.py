import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    out_lines = []
    for _ in range(t):
        x = int(data[idx])
        idx += 1

        mn = 9
        while x > 0:
            mn = min(mn, x % 10)
            x //= 10
        out_lines.append(str(mn))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
# Time Complexity: O(k) per test case, where k = number of digits in x
# Space Complexity: O(1) (excluding input storage)