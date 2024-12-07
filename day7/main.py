import itertools

with open("day7/input.txt") as f:
    content = f.readlines()

OPERAT0RS = ["+", "*"]

sum = 0
for line in content:
    result, numbers = line.strip().split(":")
    result = int(result)
    numbers = numbers.split(" ")
    numbers = [x for x in numbers if x != ""]
    numbers = [
        int(x) for x in numbers
    ]
    for idx in itertools.product(*[OPERAT0RS for x in range(len(numbers)-1)]):
        test_result = numbers[0]
        for number, operation in zip(numbers[1:], idx):
            if operation == "+":
                test_result = test_result + number
            elif operation == "*":
                test_result = test_result * number
        if test_result == result:
            sum += result
            break

print(sum)