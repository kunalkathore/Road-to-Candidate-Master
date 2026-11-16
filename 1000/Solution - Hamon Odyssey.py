t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # AND of the entire array
    total_and = a[0]
    for x in a[1:]:
        total_and &= x

    # Case 1: No benefit in splitting
    if total_and > 0:
        print(1)
        continue

    # Case 2: Greedy splitting when AND becomes zero
    curr = ~0  # all bits set
    groups = 0

    for x in a:
        curr &= x
        if curr == 0:
            groups += 1
            curr = ~0

    print(groups)

# Time Complexity:  O(n) per test case — each element is processed once.
# Space Complexity: O(n) if we consider the input and O(1) for extra space beyond input.Solution - Different Divisors


