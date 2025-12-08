with open("input.txt", "r") as f:
    raw = f.readlines()
data: list[list[str | int]] = [list(x.replace("\n", "").replace("\r", "")) for x in raw]


n = len(data)
m = len(data[0])
total = 0

for state in range(0, n-1):
    current_line = data[state]
    next_line = data[state + 1]
    for i, x in enumerate(current_line):
        if x in ["S"] or isinstance(x, int):
            y = next_line[i]
            if isinstance(y, str):
                if y == ".":
                    if isinstance(x, int):
                        if isinstance(next_line[i], int):
                            next_line[i] += x
                        else:
                            next_line[i] = x
                    else:
                        next_line[i] = 1

                if y == "^":
                    if isinstance(next_line[i-1], int):
                        next_line[i-1] += x
                    else:
                        next_line[i-1] = x
                    if isinstance(next_line[i+1], int):
                        next_line[i+1] += x
                    else:
                        next_line[i+1] = x
            elif isinstance(y, int) and isinstance(x, int):
                next_line[i] += x
                    
print(sum([x for x in data[-1] if isinstance(x, int)]))
