import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])

    # Store input lengths (input space: O(n))
    a = list(map(int, data[1:1 + n]))

    # Sort to reduce triangle check to consecutive triples
    a.sort()

    # Scan consecutive triples
    for i in range(2, n):
        if a[i - 2] + a[i - 1] > a[i]:
            sys.stdout.write("YES\n")
            return

    sys.stdout.write("NO\n")

if __name__ == "__main__":
    main()

"""
Time Complexity: O(n log n)  # sorting dominates
Space Complexity: O(n)       # storing input array
"""