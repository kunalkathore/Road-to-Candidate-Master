t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    D = s.count('-')
    U = s.count('_')

    # Need at least two '-' and one '_' to form "-_-"
    if D < 2 or U == 0:
        print(0)
        continue

    L = D // 2          # floor(D/2)
    R = D - L           # ceil(D/2)
    ans = U * L * R     # all '_' in the middle

    print(ans)

"""
Time Complexity: O(n) per test case
Space Complexity: O(1)
""" 