
import numpy as np


with open("day4/input.txt", "r") as f:
    content = f.readlines()

matrix = np.zeros((len(content), len(content[0])), dtype=str)
for i, line in enumerate(content):
    for j, char in enumerate(line):
        matrix[i, j] = char


def verify(matrix: np.array):
    if matrix[1,1] != "A":
        return False
    diag = set([matrix[0,0], matrix[2,2]])
    diag2 = set([matrix[0,2], matrix[2,0]])
    if not diag == set(("M", "S")):
        return False
    if not diag2 == set(("M", "S")):
        return False
    return True

count = 0

for i in range(0, matrix.shape[0]-2):
    for j in range(0, matrix.shape[1]-2):
        sub_matrix = matrix[i:i+3,j:j+3]
        if verify(sub_matrix):
            count+=1
print(count)
        