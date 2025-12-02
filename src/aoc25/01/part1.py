dial = [line.strip() for line in open(0).readlines()]

zeros = 0
pos = 50
sign = {"R": +1, "L": -1}
for instruction in dial:
    direction, count = instruction[0].upper(), int(instruction[1:])

    shift = sign[direction] * count
    pos = pos + shift
    if pos < 0:
        pos = 100 + pos  # pos is negative!
    pos = pos % 100
    if pos == 0:
        zeros += 1

print(zeros)
