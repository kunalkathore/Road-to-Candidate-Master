def solve():
    n = int(input())     # Length of the word
    s = input()          # The word

    res = []

    # Process from right to left
    while s:
        # If last character is a vowel → CV syllable
        if s[-1] in ('a', 'e'):
            x = 2
        # Otherwise → CVC syllable
        else:
            x = 3

        # Take last x characters
        res.append(s[-x:])
        s = s[:-x]

    # Reverse syllables and join with dots
    print('.'.join(reversed(res)))


t = int(input())         # Number of test cases
for _ in range(t):
    solve()

"""
Time Complexity:
- O(n) per test case

Space Complexity:
- O(n) for storing syllables
"""