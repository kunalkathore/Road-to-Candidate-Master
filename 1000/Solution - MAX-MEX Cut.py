def solve_string(s):
    ans = s.count('0')  # base contribution
    has0 = has1 = False

    for c in s:
        if c == '0':
            has0 = True
        if c == '1':
            has1 = True
        if has0 and has1:
            ans += 1
            has0 = has1 = False
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    ans = 0
    cur = ""

    for i in range(n):
        if a[i] != b[i]:
            ans += 2 + solve_string(cur)
            cur = ""
        else:
            cur += a[i]

    ans += solve_string(cur)
    print(ans)

# Time Complexity:  O(n) per test case
# Space Complexity: O(n) including input strings