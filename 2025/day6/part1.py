
from math import prod

with open("input.txt", "r") as f:
    data = f.readlines()

n = len(data)

numbers = []

for i in range(n):
    line = data[i]
    numbers.append([x for x in line.split() if len(x) > 0])

operations = numbers[-1]
numbers = numbers[:-1]

total = 0
for i in range(len(numbers[0])):
    numbers_line = []
    for j in range(len(numbers)):
        numbers_line.append(numbers[j][i])
    numbers_line = [int(x) for x in numbers_line]
    operation_line = operations[i]
    if operation_line == "+":
        total += sum(numbers_line)
    elif operation_line == "*":
        total += prod(numbers_line)

print(total)


