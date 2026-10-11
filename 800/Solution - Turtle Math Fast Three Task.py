t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    total_sum = sum(arr)
    rem = total_sum % 3

    # Already divisible by 3
    if rem == 0:
        print(0)
        continue

    cnt1 = 0
    cnt2 = 0

    for x in arr:
        if x % 3 == 1:
            cnt1 += 1
        elif x % 3 == 2:
            cnt2 += 1

    ans = float('inf')

    if rem == 1:
        if cnt1 > 0:
            ans = min(ans, 1)  # remove mod-1 element
        ans = min(ans, 2)      # increment twice
    else:  # rem == 2
        if cnt2 > 0:
            ans = min(ans, 1)  # remove mod-2 element
        ans = min(ans, 1)      # increment once

    print(ans)

# Time Complexity: O(n) per test case
# Space Complexity: O(1)