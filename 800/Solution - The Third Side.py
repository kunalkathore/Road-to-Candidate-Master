import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        total_sum = sum(arr)
        # Maximum possible last element
        answer = total_sum - (n - 1)
        print(answer)

if __name__ == "__main__":
    solve()

# Time Complexity: O(n) per test case (reading + summation)
# Space Complexity: O(1) extra space