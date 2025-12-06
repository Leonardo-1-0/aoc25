from collections import defaultdict


input_ = [line.split() for line in open(0).readlines()]

operators = input_[-1]
problems = defaultdict(list)
for line in input_[:-1]:
    for i, num in enumerate(map(int, line)):
        problems[i].append(num)

total = 0
for i, problem in problems.items():
    partial = problem[0]
    operator = operators[i]
    for num in problem[1:]:
        if operator == "*":
            partial *= num
        elif operator == "+":
            partial += num

    total += partial

print(total)
