from collections import defaultdict


input_ = [line.replace("\n", "") for line in open(0).readlines()]

operators = input_[-1].split()
lines = input_[:-1]

df = defaultdict(list)
for line in lines:
    for col, char in enumerate(line):
        df[col].append(char)

numbers = []
partial = 0
operator_selector = 0
total = 0
for col, digits in df.items():
    if all(digit == " " for digit in digits) or col == max(df):
        if col == max(df):
            numbers.append(int("".join(digits)))

        operator = operators[operator_selector]
        if operator == "*":
            partial = numbers[0]
            for number in numbers[1:]:
                partial *= number
        elif operator == "+":
            partial = sum(numbers)

        total += partial

        numbers = []
        operator_selector += 1
        partial = 0
        continue

    numbers.append(int("".join(digits)))

print(total)
