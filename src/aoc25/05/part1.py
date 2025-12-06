input_ = [line.strip() for line in open(0).readlines()]
ranges = input_[: input_.index("")]
ingredients = input_[input_.index("") + 1 :]


fresh = 0
for ingredient in ingredients:
    for range_ in ranges:
        start, stop = map(int, range_.split("-"))
        if start < int(ingredient) < stop:
            fresh += 1
            break

print(fresh)
