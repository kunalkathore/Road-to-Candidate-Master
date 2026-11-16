# Queen's coordinates
queenx, queeny = map(int, input().split())

# Board dimensions and positions
n = int(input())
bx, by, cx, cy = map(int, input().split())

# Function to determine quadrant relative to queen
def reg(x, y):
    ans = 0
    ans <<= 1
    ans += int(x < queenx)  # Check if x is less than queen's row
    ans <<= 1
    ans += int(y < queeny)  # Check if y is less than queen's column
    return ans

# Output YES if start and target are in the same quadrant, else NO
if reg(bx, by) != reg(cx, cy):
    print("NO")
else:
    print("YES")

# Time Complexity: O(1)
# Space Complexity: O(1)