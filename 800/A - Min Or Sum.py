t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Size of array
    a = list(map(int, input().split()))  # Read array elements

    ans = 0
    for x in a:
        ans |= x  # Bitwise OR accumulates all bits present

    print(ans)
