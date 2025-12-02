
with open("2025/day2/input.txt", "r") as f:
    data = f.read().strip()

def is_valid_id(i: int):
    number = str(i)
    n = len(number)
    for max_repeat in range(1, n//2 + 1):
        substrings = set()
        for j in range(0, n - max_repeat + 1, max_repeat):
            substring = number[j:j+max_repeat]
            if substring != number:
                substrings.add(substring)
        if len(substrings) == 1 and n%max_repeat == 0:
            return False
    return True




total = 0

for ranges in data.split(","):
    left, right = (int(x) for x in ranges.split("-"))
    for i in range(left, right + 1):
        if not is_valid_id(i):
            print(i)
            total += i

print(total)