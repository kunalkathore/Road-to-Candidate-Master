import math

tc = int(input())  # number of test cases

for _ in range(tc):
    s = input().strip()
    t = input().strip()

    n = len(s)
    m = len(t)

    # Length of the smallest possible common multiple string
    lcm_len = n * m // math.gcd(n, m)

    # Build repeated strings
    s_rep = s * (lcm_len // n)
    t_rep = t * (lcm_len // m)

    # Compare results
    if s_rep == t_rep:
        print(s_rep)
    else:
        print(-1)

# Time Complexity:
# O(LCM(|s|, |t|)) per test case — string repetition and comparison
#
# Space Complexity:
# O(LCM(|s|, |t|)) per test case — storing repeated strings