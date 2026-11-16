n, m = map(int, input().split())
s = input()
t = input()

ans = list(range(n))  # Worst case: replace all positions

for j in range(m - n + 1):
    newAns = []
    for i in range(n):
        if s[i] != t[i + j]:
            newAns.append(i)
    if len(newAns) < len(ans):
        ans = newAns

print(len(ans))
print(' '.join(str(x + 1) for x in ans))

# Time Complexity: O(n * m)
# Space Complexity: O(n)