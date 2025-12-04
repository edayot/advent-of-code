with open("input.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data if x.strip()]
    data = [list(x) for x in data]

n = len(data)
m = len(data[0])

total = 0

while True:
    number_of_neightboors = [
        [0] * m
        for _ in range(n)
    ] 

    for i in range(n):
        for j in range(m):
            val = data[i][j]
            if val == ".":
                continue
            elif val == "@":
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if k == 0 and l == 0:
                            continue
                        first = i + k
                        second = j + l
                        if not 0 <= first < n:
                            continue
                        if not 0 <= second < m:
                            continue
                        value_neightboor = data[first][second]
                        if value_neightboor == "@":
                            number_of_neightboors[first][second] += 1

    current_total = 0

    for i in range(n):
        for j in range(m):
            val = data[i][j]
            number = number_of_neightboors[i][j]
            if val == "@" and number < 4:
                current_total += 1
                data[i][j] = "."
    total += current_total
    if current_total == 0:
        break

print(total)