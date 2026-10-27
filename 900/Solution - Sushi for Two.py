import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    arr = data[1:]

    cnt = []
    run = 1
    prev = arr[0]

    for i in range(1, n):
        if arr[i] == prev:
            run += 1
        else:
            cnt.append(run)
            run = 1
            prev = arr[i]
    cnt.append(run)

    ans = 0
    for i in range(1, len(cnt)):
        ans = max(ans, 2 * min(cnt[i - 1], cnt[i]))

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()

"""
Time Complexity: O(n) (single pass + adjacent run checks)
Space Complexity: O(n) worst case for run lengths
"""