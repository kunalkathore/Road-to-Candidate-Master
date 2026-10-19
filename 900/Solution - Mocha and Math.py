import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1

        ans = int(data[idx]); idx += 1  # first element
        for _ in range(n - 1):
            ans &= int(data[idx])
            idx += 1

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# Time Complexity: O(n) per test case
# Space Complexity: O(1) (excluding input buffer)