ids = set()
for interval in open(0).read().split(","):
    start, stop = map(int, interval.split("-"))
    for digit in range(start, stop + 1):
        digit_string = str(digit)
        if len(digit_string) % 2 != 0:
            continue
        left, right = (
            digit_string[: len(digit_string) // 2],
            digit_string[len(digit_string) // 2 :],
        )
        if left == right:
            ids.add(digit_string)

print(sum(map(int, ids)))
