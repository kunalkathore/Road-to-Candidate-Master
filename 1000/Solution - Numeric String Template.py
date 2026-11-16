def solve():
    # Read size of the template array
    n = int(input())
    
    # Read the template array
    a = list(map(int, input().split()))
    
    # Number of strings to check
    m = int(input())
    
    for _ in range(m):
        # Map character -> number
        m_1 = {}
        # Map number -> character
        m_2 = {}
        
        # Read the string
        s = input().strip()
        
        # Length mismatch => cannot match
        if len(s) != n:
            print("NO")
            continue
        
        ok = True
        
        # Check one-to-one correspondence
        for j in range(n):
            if s[j] not in m_1 and a[j] not in m_2:
                # New mapping in both directions
                m_1[s[j]] = a[j]
                m_2[a[j]] = s[j]
            elif (s[j] in m_1 and m_1[s[j]] != a[j]) or \
                 (a[j] in m_2 and m_2[a[j]] != s[j]):
                # Conflict found
                ok = False
                break
        
        print("YES" if ok else "NO")


# Number of test cases
t = int(input())
for _ in range(t):
    solve()

# Time Complexity:
# For each string: O(n)
# Overall: O(sum of lengths of all strings)

# Space Complexity:
# O(n) for the two hash maps