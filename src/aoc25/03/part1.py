jolts = []
for pack in [line.strip() for line in open(0).readlines()]:
    max_ = max(pack)
    id_max = pack.index(max_)

    if max_ == pack[-1]:
        jolts.append(max(pack[:-1]) + max_)
        continue

    jolts.append(max_ + max(pack[id_max + 1 :]))

print(sum(map(int, jolts)))
