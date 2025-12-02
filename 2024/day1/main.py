


def read() -> tuple[list[int], list[int]]:
    L1, L2 = [], []
    with open("day1/sample1.txt") as f:
        lines = f.readlines()

    for line in lines:
        values = line.strip().split()
        a = values[0]
        b = values[-1]

        L1.append(int(a))
        L2.append(int(b))

    return L1, L2




def resolve1(L1: list[int], L2: list[int]):
    sum = 0
    for a, b in zip(sorted(L1), sorted(L2)):
        sum += abs(a-b)
    return sum

def resolve2(L1: list[int], L2: list[int]):
    sum = 0 
    for a in L1:
        occur = 0
        for b in L2:
            if a == b:
                occur += 1
        sum += occur * a
    return sum




L1, L2 = read()
res = resolve2(L1, L2)
print(res)