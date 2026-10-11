t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    # Count total number of '0's
    count_zero = s.count('0')

    # Count misplaced '1's in the first count_zero positions
    misplaced = 0
    for i in range(count_zero):
        if s[i] == '1':
            misplaced += 1

    # Minimum operations required
    print(misplaced)

# Time Complexity (TC):
# - O(n) per test case
#   (counting zeros + scanning prefix)

# Space Complexity (SC):
# - O(n) per test case
#   (for the input string)