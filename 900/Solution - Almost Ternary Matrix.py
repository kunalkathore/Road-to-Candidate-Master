import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx]); m = int(data[idx + 1])
        idx += 2

        for i in range(1, n + 1):
            row_flag = (i % 4 == 0) or (i % 4 == 1)
            row_vals = []
            for j in range(1, m + 1):
                col_flag = (j % 4 == 0) or (j % 4 == 1)
                val = 1 if (row_flag != col_flag) else 0
                row_vals.append(str(val))
            out_lines.append(" ".join(row_vals))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

# Time Complexity: O(t * n * m)
# Space Complexity: O(1) extra space (excluding output storage)