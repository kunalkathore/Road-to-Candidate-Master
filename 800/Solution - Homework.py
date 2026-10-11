def solve():
    # Read integer n and string a
    n = int(input())
    a = input().strip()
    
    # Read integer m, string b, and string c
    m = int(input())
    b = input().strip()
    c = input().strip()
    
    # List to store characters that will be added to the left side
    add_left = []
    
    # Traverse string b and c
    for i in range(m):
        if c[i] == 'V':
            # Store characters that should be added to the left side
            add_left.append(b[i])
        else:
            # Directly append characters to the right side of string a
            a += b[i]
    
    # Reverse the left-side characters
    add_left.reverse()
    
    # Output the final constructed string
    print("".join(add_left) + a)


# Main execution
t = int(input())  # Number of test cases
for _ in range(t):
    solve()


"""
Time Complexity (TC):
O(m) per test case
- Single traversal of string b
- One reverse of left part

Space Complexity (SC):
O(n + m)
- a, b, c strings (input space)
- add_left list (auxiliary space)
"""