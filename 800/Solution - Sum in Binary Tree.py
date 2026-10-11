import sys

def solve():
    # Read n, ensuring it's treated as an integer
    # Python handles large integers automatically
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    total_sum = 0
    
    # Traverse from node n up to the root
    while n > 0:
        total_sum += n  # Add current node
        n //= 2         # Move to parent (integer division)
        
    print(total_sum)

def main():
    # Read number of test cases
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

# Time Complexity: O(log n) per test case
# Space Complexity: O(1)