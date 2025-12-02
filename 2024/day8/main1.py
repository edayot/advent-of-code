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
            antinode1: tuple[int, int] = (x+gap[0], y+gap[1])
            antinode2: tuple[int, int] = (i-gap[0], j-gap[1])

            if is_inbound(content, antinode1):
                content[antinode1[0]][antinode1[1]] = "#"
            if is_inbound(content, antinode2):
                content[antinode2[0]][antinode2[1]] = "#"
res = content_str(content) 
print(res)
print(res.count("#"))