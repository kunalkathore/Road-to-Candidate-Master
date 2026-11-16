import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    d = int(data[1])
    p = list(map(int, data[2:]))

    p.sort(reverse=True)

    i = 0
    j = n - 1
    wins = 0

    while i <= j:
        captain = p[i]
        k = (d // captain) + 1       # minimal size to make k * captain > d
        need_fillers = k - 1

        if i + need_fillers <= j:
            wins += 1
            i += 1
            j -= need_fillers
        else:
            break

    print(wins)

if __name__ == "__main__":
    main()

"""
Time Complexity: O(N log N)
Space Complexity: O(N)
"""