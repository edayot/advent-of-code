
from copy import deepcopy
from enum import Enum
from typing import Literal, Optional
from tqdm import trange
from rich import print
import sys
sys.setrecursionlimit(10**5)

OBSTACLES = set(["#", "O"])
GUARD = ["^", "v", ">", "<"]
PATH = "X"


def find_guard(content: list[list[str]]) -> tuple[tuple[int, int] | None, tuple[int, int] | None]:
    for i, line in enumerate(content):
        for j, value in enumerate(line):
            if value in GUARD:
                return (i, j), find_new_pos(i, j, value)
    return None, None

def find_new_pos(i: int, j: int, value: str):
    match value:
        case "^":
            return (i-1, j)
        case "v":
            return (i+1, j)
        case ">":
            return (i, j+1)
        case "<":
            return (i, j-1)
        
    raise ValueError(value)


def rotate_right(direction: Literal["^", "v", ">", "<"] | str) -> Literal["^", "v", ">", "<"]:
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

def is_inbound(content: list[list[str]], pos: tuple[int, int]):
    if pos[0] >= len(content) or pos[0] < 0:
        return False
    if pos[1] >= len(content[0]) or pos[1] < 0:
        return False
    return True


def run(content: list[list[str]], current: Optional[tuple[int, int]] = None):
    # Init variables
    if current is None:
        current, new = find_guard(content)
    else: 
        new = find_new_pos(current[0], current[1], content[current[0]][current[1]])

    # Stop condition
    if not current or not new:
        return 
    if not is_inbound(content, new):
        content[current[0]][current[1]] = "X"
        return 
    
    # iterating
    if not content[new[0]][new[1]] == "#":
        content[new[0]][new[1]] = content[current[0]][current[1]]
        content[current[0]][current[1]] = "X"
        return run(content, new)
    else:
        content[current[0]][current[1]] = rotate_right(content[current[0]][current[1]])
        
        return run(content, current)



def is_stucking_position(content: list[list[str]]):
    try:
        run(content)
        return False
    except RecursionError:
        return True





with open('day6/input.txt') as f:
    data = f.read().splitlines()

content : list[list[str]] = []
for line in data:
    content.append([])
    for char in line:
        content[-1].append(char)



# Part One
i=0
pos = None
temp = deepcopy(content)

run(temp)

sum = 0
for i in range(len(temp)):
    for j in range(len(temp[0])):
        if temp[i][j] == "X":
            sum+=1
print(sum)


# Part Two
sum = 0
for i in trange(len(content)):
    for j in range(len(content[0])):
        new_content = deepcopy(content)
        new_content[i][j] = "#"
        if is_stucking_position(new_content):
            sum+=1

print(sum)