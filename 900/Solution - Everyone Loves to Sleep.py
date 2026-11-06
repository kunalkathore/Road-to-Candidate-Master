t = int(input()) 
for _ in range(t):
    n, H, M = map(int, input().split())

    # Convert current time to minutes
    current_time = H * 60 + M

    # Maximum waiting time in a day
    min_wait = 24 * 60

    for _ in range(n):
        h, m = map(int, input().split())

        # Convert alarm time to minutes
        alarm_time = h * 60 + m

        # Time difference
        diff = alarm_time - current_time

        # If alarm is before current time, it rings next day
        if diff < 0:
            diff += 24 * 60

        # Update minimum wait time
        min_wait = min(min_wait, diff)

    # Output hours and minutes
    print(min_wait // 60, min_wait % 60)

"""
Time Complexity:
O(n) per test case.

Space Complexity:
O(1) extra space.
"""