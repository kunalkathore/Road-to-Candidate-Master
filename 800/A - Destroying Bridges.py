t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # n islands, k bridges can be destroyed

    # To isolate island 1, we need to destroy all (n-1) bridges connected to it
    if k >= n - 1:
        # Island 1 becomes completely isolated
        print(1)
    else:
        # Not enough bridges destroyed, graph remains connected
        print(n)

# Time Complexity (TC): O(1) per test case
# Space Complexity (SC): O(1) per test case