import sys

def is_balanced_middle(s: str) -> bool:
    # Check substring s[1 ... n-2] for balanced bracket sequence property
    n = len(s)
    bal = 0

    for i in range(1, n - 1):
        if s[i] == '(':
            bal += 1
        else:
            bal -= 1

        # Negative prefix balance means not balanced
        if bal < 0:
            return False

    return bal == 0

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    out_lines = []
    for _ in range(t):
        s = data[idx]
        idx += 1

        middle_ok = is_balanced_middle(s)
        out_lines.append("NO" if middle_ok else "YES")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()

"""
Time Complexity (per test case): O(n)  # one scan over the string middle
Space Complexity (per test case): O(n) # storing input string s (counting input)
"""