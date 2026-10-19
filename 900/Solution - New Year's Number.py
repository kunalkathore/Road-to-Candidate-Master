import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        # q = how many full 2020 blocks we can take from n
        q = n // 2020

        # r = remainder after dividing n by 2020
        # This remainder is the best candidate for y (count of 2021)
        r = n % 2020

        # If we take y = r, then remaining 2020 count becomes:
        # x = q - r
        # We need x >= 0  =>  q >= r
        if r <= q:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# Time Complexity: O(1) per test case
# Space Complexity: O(1) per test case