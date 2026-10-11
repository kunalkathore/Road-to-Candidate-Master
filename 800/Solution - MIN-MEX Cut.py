t = int(input())  # Read the number of test cases

for _ in range(t):
    s = input().strip()  # Read the binary string

    # Count the total number of '0's
    total_zeroes = s.count('0')

    # If there are no zeroes, no operations are needed
    if total_zeroes == 0:
        print(0)
        continue

    # Find first and last occurrence of '0'
    first_zero_index = s.find('0')
    last_zero_index = s.rfind('0')

    # Check if all zeroes are contiguous
    if last_zero_index - first_zero_index + 1 == total_zeroes:
        print(1)
    else:
        print(2)

# Time Complexity (TC): O(n) per test case
# Space Complexity (SC): O(n) for the input string in each test case