import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        m = int(data[idx]); idx += 1

        # Fake starting requirement: time = 0, side = 0
        prev_a = 0
        prev_b = 0

        ans = 0  # total points (total minutes we run)

        for _ in range(n):
            a = int(data[idx]); idx += 1
            b = int(data[idx]); idx += 1

            # Minutes available in this segment
            d = a - prev_a

            # need = 0 if same side, 1 if side changes
            need = abs(b - prev_b)

            # Try to run every minute => d points
            ans += d

            # If parity mismatch, we must stay exactly once => -1 point
            if (d % 2) != (need % 2):
                ans -= 1

            # Move to next segment
            prev_a = a
            prev_b = b

        # After last requirement, run every remaining minute
        ans += (m - prev_a)

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

"""
Time Complexity: O(n) per test case (plus input reading)
Space Complexity: O(1) extra space (excluding input storage)
"""