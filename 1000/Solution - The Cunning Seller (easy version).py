# Precompute cost for deals of size 3^k
cost = []
c = 3       # cost for 3^0 deal
cnt = 1     # keeps track of 3^(k-1)

for _ in range(21):  # 3^20 > 10^9
    cost.append(c)
    c = 3 * c + cnt  # 3^(k+1) + k*3^(k-1)
    cnt *= 3         

t = int(input())
for _ in range(t):
    n = int(input())
    min_k = 0
    min_cost = 0
    sz = 0
    
    while n:
        digit = n % 3
        min_k += digit
        min_cost += digit * cost[sz]
        n //= 3
        sz += 1

    print(min_cost)

"""
Time Complexity: O(log_3 n) per test case
Space Complexity: O(log_3 n) for precomputed cost list
"""