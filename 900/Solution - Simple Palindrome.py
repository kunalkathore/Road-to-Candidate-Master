import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    vowels = "aeiou"
    out_lines = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        # Distribute n evenly among 5 vowels.
        base = n // 5
        rem = n % 5

        # Build 5 blocks: a...e...i...o...u...
        parts = []
        for i in range(5):
            cnt = base + (1 if i < rem else 0)
            parts.append(vowels[i] * cnt)

        out_lines.append("".join(parts))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

"""
Time Complexity (per test case): O(n)  # building + printing n characters
Space Complexity (per test case): O(n) # output string length n 
"""