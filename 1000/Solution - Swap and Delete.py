import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    out = []

    for _ in range(t):
        s = input_data[idx]
        idx += 1
        n = len(s)

        cnt0 = s.count('0')
        cnt1 = n - cnt0

        built = 0
        for i, ch in enumerate(s):
            # Need opposite of ch at this position
            if ch == '0':
                if cnt1 == 0:
                    break
                cnt1 -= 1
            else:
                if cnt0 == 0:
                    break
                cnt0 -= 1
            built += 1

        out.append(str(n - built))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# Time Complexity: O(sum |s|)
# Space Complexity: O(1) extra