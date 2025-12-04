with open("input.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data if x.strip()]

n = len(data)
m = len(data[0])

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

total = 0

for i in range(n):
    for j in range(m):
        val = data[i][j]
        number = number_of_neightboors[i][j]
        if val == "@" and number < 4:
            total += 1

print(total)