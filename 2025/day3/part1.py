with open("2025/day3/input.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data if x.strip()]

def iterate_line(line: str):
    already: set[str] = set()
    for i in range(len(line)):
        if line[i] in already:
            continue
        already.add(line[i])
        already_line: set[str] = set()
        for j in range(i+1, len(line)):
            if line[j] in already_line:
                continue
            yield int(line[i] + line[j])


def resolve_line(line: str):
    return max(iterate_line(line))

total = 0
for line in data:
    x = resolve_line(line)
    total += x

print(total)
