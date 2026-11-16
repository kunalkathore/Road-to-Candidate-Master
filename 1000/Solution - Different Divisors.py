# Function to solve one test case
def solve():
    x = int(input())          # Read the value of d

    primes = []               # To store primes p and q

    # Find the smallest prime p such that p >= x + 1
    i = x + 1
    while True:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            break
        i += 1

    # Find the smallest prime q such that q >= p + x
    i = primes[0] + x
    while True:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            break
        i += 1

    # Output minimum of p*q and p^3
    print(min(primes[0] * primes[1], primes[0] ** 3))


t = int(input())              # Number of test cases
for _ in range(t):
    solve()

"""
Time Complexity (Python): O(t * sqrt(d))
Space Complexity (Python): O(1)
"""