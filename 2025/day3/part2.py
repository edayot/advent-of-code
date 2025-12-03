
from functools import cache

if True:
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


total = 0
for i, line in enumerate(data):
    x = resolve_line(line)
    if sample_ok and i < len(sample_ok):
        expected = sample_ok[i]
        print(f"{line=}, {x=}, {len(x)=}, {expected=}, {expected == x}")
        total += int(x)
    elif sample_ok:
        print(f"{line=}, {x=}")
    else:
        total += int(x)


    

print("sum=", total)
print("sample OK : ", 3121910778619 == total)