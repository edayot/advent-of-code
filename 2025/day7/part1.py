with open("input.txt", "r") as f:
    raw = f.readlines()
data: list[list[str]] = [list(x.replace("\n", "").replace("\r", "")) for x in raw]


n = len(data)
m = len(data[0])
total = 0

for state in range(0, n-1):
    current_line = data[state]
    next_line = data[state + 1]
    for i, x in enumerate(current_line):
        if x in ["S", "|"]:
            y = next_line[i]
            match y:
                case ".":
                    next_line[i] = "|"
                case "^":
                    next_line[i-1] = "|"
                    next_line[i+1] = "|"
                    total += 1

print(total)
