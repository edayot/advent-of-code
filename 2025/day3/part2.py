
from functools import cache

if False:
    with open("sample.txt", "r") as f:
        data = f.readlines()
        data = [x.strip() for x in data if x.strip()]
    with open("sample_ok.txt", "r") as f:
        sample_ok = f.readlines()
        sample_ok = [x.strip() for x in sample_ok if x.strip()]
else:
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [x.strip() for x in data if x.strip()]
    sample_ok = None



def add_trailing_zeros(x: str):
    return "0" * (12 - len(x)) + x

def iterate_line(line: str, n: int):
    already = set()
    for i in range(len(line)):
        left = line[i]
        right = line[i+1:]
        if left in already and n != 1:
            continue
        already.add(left)
        if not right:
            yield left
        elif len(right) == 1 or n == 1:
            yield (left + right[0])
        else:
            yield left + resolve_line(right, n-1)


def resolve_line(line: str, n = 11):
    M = ""
    m = ""
    for x in iterate_line(line, n):
        if add_trailing_zeros(x) > M:
            M = add_trailing_zeros(x)
            m = x
    return m

def solve_row(row: list[int], max_batteries: int) -> int:
    # triche
    result, start = 0, 0    
    length = len(row)
    for digit_pos in range(max_batteries):
        end = length - (max_batteries - digit_pos) + 1
        max_digit = max(row[start:end])
        start = row.index(max_digit, start, end) + 1
        result = result * 10 + max_digit
    return result


total = 0
for i, line in enumerate(data):
    x = solve_row([int(c) for c in line], 12)
    total += int(x)


    

print("sum=", total)
print("sample OK : ", 3121910778619 == total)