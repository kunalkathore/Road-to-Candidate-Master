import sys

input = sys.stdin.readline  # Fast input method

t = int(input())  # Number of test cases

while t > 0:
    t -= 1

    n = int(input())  # Length of the string
    s = input().strip()  # String representing the cells

    empty_cells = 0  # Variable to count empty cells
    found_three_consecutive = False  # Flag to check "..."

    for i in range(n):  # Loop through the string
        if s[i] == '.':  # If current cell is empty
            empty_cells += 1  # Increase count

        # Check for three consecutive empty cells
        if i >= 2 and s[i] == '.' and s[i - 1] == '.' and s[i - 2] == '.':
            found_three_consecutive = True  # Condition satisfied
            break  # Exit loop

    if found_three_consecutive:  # If "..." exists
        answer = 2
    else:
        answer = empty_cells  # Otherwise total empty cells

    print(answer)  # Output the answer

# Time Complexity (TC): O(n) per test case
# Space Complexity (SC): O(n) per test case