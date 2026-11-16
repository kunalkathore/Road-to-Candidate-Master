import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n

        # Odd n: Mike wins by emptying pile 1 immediately.
        if n % 2 == 1:
            out.append("Mike")
            continue

        # Even n: find earliest index of the minimum element.
        pos = 0
        for i in range(1, n):
            if a[i] < a[pos]:
                pos = i

        # pos even (0-based) => Mike's pile => Joe wins, else Mike wins.
        out.append("Joe" if pos % 2 == 0 else "Mike")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# Time Complexity: O(n) per test case
# Space Complexity: O(1) extra (excluding input storage)