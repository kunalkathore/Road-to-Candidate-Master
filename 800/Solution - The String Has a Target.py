import sys

def smallest_after_move_to_front(s: str) -> str:
    # 1) Minimum character decides the best possible first character
    min_char = min(s)

    # 2) Best occurrence to move is the LAST occurrence of min_char
    pos = s.rfind(min_char)

    # 3) Construct: s[pos] + s[:pos] + s[pos+1:]
    return s[pos] + s[:pos] + s[pos + 1:]

def solve() -> None:
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        s = data[idx]; idx += 1
        out.append(smallest_after_move_to_front(s))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# Time Complexity: O(n) per test case
# Space Complexity: O(n) per test case