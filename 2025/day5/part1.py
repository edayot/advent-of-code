with open("input.txt", "r") as f:
    data = f.readlines()

ranges = []
ingredient_ids = []

in_ranges = True

for line in data:
    value = line.strip()
    if not value:
        in_ranges = False
        continue
    if in_ranges:
        m, M = (int(x) for x in value.split("-"))
        ranges.append((m, M))
    else:
        ingredient_ids.append(int(value))


total = 0
for ingredient_id in ingredient_ids:
    for m, M in ranges:
        if m <= ingredient_id <= M:
            total += 1
            break

print(total)

