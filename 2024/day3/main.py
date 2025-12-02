import re


with open("day3/input.txt") as f:
    content = f.read()

regex = re.compile(r"mul\((\d+),(\d+)\)")
do_dont_regex = re.compile(r"don't\(\)|do\(\)")

sum1 = 0

for match in regex.findall(content):
    mul = int(match[0]) * int(match[1])
    sum1+=mul

print(sum1)

sum2 = 0
do_dont = list(do_dont_regex.finditer(content))
do_dont.reverse()

for match in regex.finditer(content):
    index_start = match.start(0)
    is_precedded_by_do = True
    for math_dont in do_dont:
        if math_dont.start(0) > index_start:
            continue
        if math_dont.group(0) == "don't()":
            is_precedded_by_do = False
        elif math_dont.group(0) == "do()":
            break
    if not is_precedded_by_do:
        continue
    mul = match.groups()
    sum2 += int(mul[0]) * int(mul[1])

print(sum2)