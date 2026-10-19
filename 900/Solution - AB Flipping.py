import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = data[idx]  # storing the string takes O(n) space
        idx += 1

        # Find x = first position of 'A'
        x = -1
        for i, ch in enumerate(s):
            if ch == 'A':
                x = i
                break

        # Find y = last position of 'B'
        y = -1
        for i in range(n - 1, -1, -1):
            if s[i] == 'B':
                y = i
                break

        # Apply the final rule
        if x != -1 and y != -1 and x < y:
            out.append(str(y - x))
        else:
            out.append("0")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

"""
Time Complexity: O(n) per test case, total O(sum n)
Space Complexity: O(n) per test case (to store the string)
"""