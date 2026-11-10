import sys

def solve():
    data = sys.stdin.read().strip().split()
    q = int(data[0])
    idx = 1

    out_lines = []
    for _ in range(q):
        s = data[idx]
        t = data[idx + 1]
        idx += 2

        # Case 1
        if t == "a":
            out_lines.append("1")
            continue

        # Case 2: if t contains 'a' then infinite
        if 'a' in t:
            out_lines.append("-1")
            continue

        # Case 3: t has no 'a'
        n = len(s)
        out_lines.append(str(1 << n))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

"""
Time Complexity:
Per testcase: O(|s| + |t|) (input + 'a' membership scan), overall O(q*(|s|+|t|)).

Space Complexity:
O(total input size) for reading all tokens, plus O(1) extra per testcase.
"""