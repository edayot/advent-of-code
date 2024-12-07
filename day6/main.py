
from enum import Enum
from typing import Literal
import numpy as np


def find_guard_new_position(matrix: np.array) -> tuple[tuple[int, int], tuple[int, int]]:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            match matrix[i, j]:
                case "^":
                    return (i, j), (i-1, j)
                case "v":
                    return (i, j), (i+1, j)
                case ">":
                    return (i, j), (i, j+1)
                case "<":
                    return (i, j), (i, j-1)
                case _:
                    continue
    return None, None

def rotate_right(direction: Literal["^", "v", ">", "<"]) -> Literal["^", "v", ">", "<"]:
    match direction:
        case "^":
            return ">"
        case "v":
            return "<"
        case ">":
            return "v"
        case "<":
            return "^"
        case _:
            raise ValueError("Unknow direction, {direction}")

def is_inbound(matrix: np.array, pos: tuple[int, int]):
    if pos[0] >= matrix.shape[0] or pos[0] < 0:
        return False
    if pos[1] >= matrix.shape[1] or pos[1] < 0:
        return False
    return True


def tour(matrix: np.array):
    current, new = find_guard_new_position(matrix)
    if not current or not new:
        return False
    if not is_inbound(matrix, new):
        matrix[current] = "X"
        return False
    if not matrix[new] == "#":
        matrix[new] = matrix[current]
        matrix[current] = "X"
    else:
        matrix[current] = rotate_right(matrix[current])
    return True




with open('day6/input.txt') as f:
    content = f.read().splitlines()


matrix = np.zeros((len(content), len(content[0])), dtype=str)
for i, line in enumerate(content):
    for j, char in enumerate(line):
        matrix[i, j] = char


running = True
i=0
while running:
    # print(matrix)
    # input(f"Press enter for next tour ({i}/?)")
    running = tour(matrix)
    i+=1
print(matrix)

sum = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == "X":
            sum+=1
print(sum)