

with open("day9/input.txt") as f:
    content = f.read().strip()


def transform(content: str):
    for i in range(len(content)):
        if i%2 == 0:
            for _ in range(int(content[i])):
                yield str(i//2)
        else:
            for _ in range(int(content[i])):
                yield "."

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
print(sum)


