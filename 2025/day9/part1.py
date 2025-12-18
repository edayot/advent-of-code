from typing import NamedTuple
from math import prod
from rich import print

class Tile(NamedTuple):
    x: int
    y: int

def area(t1: Tile, t2: Tile):
    return abs((t1.x - t2.x + 1)*(t1.y - t2.y + 1))

with open("input.txt", "r") as f:
    raw = f.readlines()


tiles: list[Tile] = []
for line in raw:
    x, y = line.split(",")
    x, y = int(x), int(y)
    tiles.append(Tile(y, x))


candidates: list[tuple[Tile, Tile]] = []

for t1 in tiles:
    for t2 in tiles:
        candidates.append((t1, t2))

res = max(candidates, key=lambda x: area(x[0], x[1]))
print(res, area(res[0], res[1]))

# for i in range(9):
#     for j in range(15):
#         if Tile(i, j) in res:
#             print("O", end="")
#         elif Tile(i, j) in tiles:
#             print("X", end="")
#         else:
#             print(".", end="")   
#     print()