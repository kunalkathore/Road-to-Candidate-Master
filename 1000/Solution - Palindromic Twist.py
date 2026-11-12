# Read number of test cases
T = int(input())

for _ in range(T):
    n = int(input())
    s = input()
    
    ok = True
    
    # Check mirrored character pairs
    for i in range(n):
        diff = abs(ord(s[i]) - ord(s[n - i - 1]))
        
        # Invalid if distance is odd or greater than 2
        if diff > 2 or diff % 2 == 1:
            ok = False
            break
    
    # Print result
    print("YES" if ok else "NO")

"""
Time Complexity:
- O(T * n)

Space Complexity:
- O(1) extra space
"""