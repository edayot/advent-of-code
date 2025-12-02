
with open("2025/day2/input.txt", "r") as f:
    data = f.read().strip()

def is_valid_id(i: int):
    number = str(i)
    n = len(number)
    if n%2 == 1:
        return True
    left = number[:n//2]
    right = number[n//2:]
    return left != right

total = 0

for ranges in data.split(","):
    left, right = (int(x) for x in ranges.split("-"))
    for i in range(left, right + 1):
        if not is_valid_id(i):
            total += i

print(total)
