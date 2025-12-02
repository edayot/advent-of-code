

with open("day9/sample.txt") as f:
    content = f.read().strip()


def transform(content: str):
    for i in range(len(content)):
        if i%2 == 0:
            for _ in range(int(content[i])):
                yield str(i//2)
        else:
            for _ in range(int(content[i])):
                yield "."


def part1(content):
    content = list(transform(content))
    x = 0
    y = len(content)-1
    while x<y:
        while content[x] != ".":
            x+=1
        while content[y] == ".":
            y-=1
        content[x], content[y] = content[y], content[x]
    content[x], content[y] = content[y], content[x]

    content = [int(x) for x in content if x != "."]

    sum = 0
    for i, x in enumerate(content):
        sum += i * x
    # print(sum)



def part2(content):
    content = list(transform(content))
    
    for y in range(len(content))[::-1]:
        value = content[y]
        if value == ".":
            continue
        if y != len(content)-1:
            if content[y+1] == value:
                continue
        y_left = y
        y_right = y + 1
        while content[y_left] == value:
            y_left-=1
        y_left+=1
        space_needed = y_right - y_left
        x_left, x_right = None, None

        for x in range(0, len(content)):
            if content[x] != ".":
                continue
            if not all([
                v == "."
                for v in content[x:x+space_needed]
            ]):
                continue
            x_left = x
            x_right = x + space_needed
            break
        if x_left is None or x_right is None:
            continue
        if x_right >= len(content):
            continue
        for i in range(x_left, x_right):
            content[i] = value
        for i in range(y_left, y_right):
            content[i] = "."    
        break
    print("".join(content), y)






part1(content)
part2(content)