with open("input.txt", "r") as f:
    data = f.readlines()

ranges = set()
in_ranges = True

for line in data:
    value = line.strip()
    if not value:
        in_ranges = False
        continue
    if in_ranges:
        m, M = (int(x) for x in value.split("-"))
        ranges.add((m, M))

print(ranges)
initial = 0
while initial != len(ranges):
    initial = len(ranges)
    to_remove = set()
    to_add = set()
    for m1, M1 in ranges:
        for m2, M2 in ranges:
            if m1 == m2 and M1 == M2:
                continue
            m1_in_2 = m2 <= m1 <= M2
            M1_in_2 = m2 <= M1 <= M2
            if m1_in_2 and M1_in_2:
                to_remove.add((m1, M1))
            elif m1_in_2 and not M1_in_2:
                to_remove.add((m1, M1))
                to_remove.add((m2, M2))

                to_add.add((m2, M1))
            elif not m1_in_2 and M1_in_2:
                to_remove.add((m1, M1))
                to_remove.add((m2, M2))

                to_add.add((m1, M2))

    for x in to_remove:
        ranges.remove(x)
    for y in to_add:
        ranges.add(y)

total = 0
for m, M in ranges:
    total += M-m + 1

print(total)