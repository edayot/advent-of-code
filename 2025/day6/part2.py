from math import prod

with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.replace("\n", "").replace("\r", "") for x in data]

n = len(data)
m = len(data[0])

numbers = []
total = 0

for j in range(m-1, -1, -1):
    current_number = ""
    for i in range(0, n - 1):
        current_number += data[i][j]
    current_number = current_number.strip()
    if current_number:
        numbers.append(int(current_number))
    if (operation := data[n-1][j]) != " ":
        if operation == "+":
            total += sum(numbers)
        elif operation == "*":
            total += prod(numbers)
        numbers = []

print(total)
