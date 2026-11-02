MOD = 10**9 + 7
N = 10**5 + 5

# Precompute factorials modulo MOD
fact = [1] * N
for i in range(1, N):
    fact[i] = (fact[i-1] * i) % MOD

t = int(input())   # Number of test cases
for _ in range(t):
    n = int(input())

    # Beauty of one permutation
    ans = n * (n - 1) % MOD

    # Multiply by n! to get sum over all permutations
    ans = (ans * fact[n]) % MOD

    print(ans)

"""
Time Complexity:
- Precomputation of factorials: O(N)
- Per test case: O(1)
Space Complexity:
- O(N) for factorial array
"""