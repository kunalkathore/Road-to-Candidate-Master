import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        c = data[idx][0]    # store as int (ASCII code)
        idx += 1
        s = data[idx]       # bytes of length n
        idx += 1

        # If current color is green, answer is 0.
        if c == ord('g'):
            out_lines.append("0")
            continue

        # Duplicate string to handle cyclicity; bytes concatenation keeps it fast.
        s2 = s + s

        last_g = -1
        ans = 0
        g_code = ord('g')

        # Scan right-to-left.
        for i in range(2 * n - 1, -1, -1):
            if s2[i] == g_code:
                last_g = i
            if i < n and s2[i] == c:
                ans = max(ans, last_g - i)

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

"""
Time Complexity:
- O(n) per test case (scan 2n positions once).
- O(sum n) overall.

Space Complexity:
- O(n) for input string s and duplicated string s2.

"""