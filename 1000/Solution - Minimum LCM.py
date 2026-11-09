import sys
import math

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    out_lines = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1

        a = 1  # Default for prime n
        limit = int(math.isqrt(n))

        # Find the smallest divisor g >= 2
        for g in range(2, limit + 1):
            if n % g == 0:
                # Largest divisor <= n/2
                a = n // g
                break

        b = n - a
        out_lines.append(f"{a} {b}")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

"""
Time Complexity (per test case): O(sqrt(n))  # checking divisors up to isqrt(n)
Space Complexity (per test case): O(1)       # constant extra variables; input is one integer n
"""