import math
import re


ids = set()
for interval in open(0).read().split(","):
    start, stop = map(int, interval.split("-"))
    for digit in range(start, stop + 1):
        digit_string = str(digit)
        for i in range(1, math.ceil(len(digit_string))):
            sequence = digit_string[:i]
            if re.sub(sequence, "", digit_string) == "":
                ids.add(digit_string)

print(sum(map(int, ids)))
