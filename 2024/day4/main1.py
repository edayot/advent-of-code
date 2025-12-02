
import numpy as np


with open("day4/input.txt", "r") as f:
    content = f.readlines()

matrix = np.zeros((len(content), len(content[0])), dtype=str)
for i, line in enumerate(content):
    for j, char in enumerate(line):
        matrix[i, j] = char

xmas = "XMAS"
samx = "".join(xmas[::-1])

count = 0
for line in matrix:
    line_string = "".join(line)
    count += line_string.count(xmas)
    count += line_string.count(samx)

for column in matrix.T:
    column_string = "".join(column)
    count += column_string.count(xmas)
    count += column_string.count(samx)

for diagonal_index in range(-matrix.shape[0]*matrix.shape[1], matrix.shape[0]*matrix.shape[1]):
    diagonal = matrix.diagonal(diagonal_index)
    diagonalR = np.fliplr(matrix).diagonal(diagonal_index)
    diagonal_string = "".join(diagonal).strip()
    diagonalR_string = "".join(diagonalR).strip()
    if len(diagonal_string) > 0:
        print(diagonal_string, diagonalR_string)

    count += diagonal_string.count(xmas)
    count += diagonal_string.count(samx)
    count += diagonalR_string.count(xmas)
    count += diagonalR_string.count(samx)

print(count)