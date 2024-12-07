
from copy import deepcopy
from enum import Enum
from typing import Literal, Optional
from tqdm import trange
from rich import print

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


def run(content: list[list[str]], current: Optional[tuple[int, int]] = None, max_depth: int = 100):
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
        return run(content, new, max_depth=max_depth-1)
    else:
        content[current[0]][current[1]] = rotate_right(content[current[0]][current[1]])
        
        return run(content, current, max_depth=max_depth-1)



def is_stucking_position(content: list[list[str]]):
    seen_position = set()
    running = True
    i=0
    pos = None
    while running:
        pos = run(content, pos)
        if pos is None:
            return False, i
        if pos in seen_position:
            break
        seen_position.add(pos)
        i+=1
    return True, i





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
import sys
sys.setrecursionlimit(10**5)
run(content)

sum = 0
for i in range(len(content)):
    for j in range(len(content[0])):
        if content[i][j] == "X":
            sum+=1
print(sum)

