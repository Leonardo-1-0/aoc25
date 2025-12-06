intervals = []
for line in open(0).readlines():
    line = line.strip()
    if not line:
        break
    intervals.append(tuple(map(int, line.split("-"))))

intervals = sorted(intervals)

top, ids = -1, 0
for low, high in intervals:
    if low > high:
        low, high = high, low

    if top < low:
        delta = (high - low) + 1
    elif top < high:
        delta = high - top
    top = high

print(ids)
