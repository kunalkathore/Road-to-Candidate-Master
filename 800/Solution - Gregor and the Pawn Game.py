import sys

def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        enemy = list(input().strip())
        gregor = input().strip()
        used = [False] * n
        ans = 0
        for i, ch in enumerate(gregor):
            if ch == '0':
                continue
            # capture left
            if i > 0 and enemy[i-1] == '1' and not used[i-1]:
                used[i-1] = True
                ans += 1
            # forward
            elif enemy[i] == '0':
                ans += 1
            # capture right
            elif i + 1 < n and enemy[i+1] == '1' and not used[i+1]:
                used[i+1] = True
                ans += 1
            # else stuck
        print(ans)

if __name__ == "__main__":
    solve()

# Time Complexity: O(n) per test case
# Space Complexity: O(n) for used[]