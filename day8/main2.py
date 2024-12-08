from rich import print

with open('day8/input.txt') as f:
    data = f.read().splitlines()

content : list[list[str]] = []
for line in data:
    content.append([])
    for char in line:
        content[-1].append(char)

antenna_to_pos: dict[str, list[tuple[int, int]]] = {}

for i in range(len(content)):
    for j in range(len(content[0])):
        value = content[i][j]
        if value == ".":
            continue
        antenna_to_pos.setdefault(value, []).append(
            (i, j)
        )

def content_str(content: list[list[str]]):
    return ("\n".join([
        "".join(line)
        for line in content
    ]))


def is_inbound(content: list[list[str]], pos: tuple[int, int]):
    if pos[0] >= len(content) or pos[0] < 0:
        return False
    if pos[1] >= len(content[0]) or pos[1] < 0:
        return False
    return True

for antenna in antenna_to_pos.keys():
    for (x, y) in antenna_to_pos[antenna]:
        for (i, j) in antenna_to_pos[antenna]:
            gap: tuple[int, int] = (x-i, y-j)
            if gap[0] == 0 and gap[1] == 0:
                continue

            n = len(content)*len(content[0])
            for i in range(-n, n):
                new_gap = (gap[0]*i, gap[1]*i)
                antinode: tuple[int, int] = (x+new_gap[0], y+new_gap[1])
                if is_inbound(content, antinode):
                    content[antinode[0]][antinode[1]] = "#"

res = content_str(content) 
print(res)
print(res.count("#"))