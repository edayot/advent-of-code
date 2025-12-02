


def read():
    with open('day2/input.txt', "r") as f:
        content = f.readlines()
    L = []
    for x in content:
        L.append([int(y) for y in x.split(" ")])
    return L
    


    

def solve1(L: list[list[int]]):
    sum = 0
    for report in L:
        if is_safe1(report):
            sum+=1
    return sum

def is_safe1(report: list[int]):
    is_increasing = True
    is_decreasing = True
    increase = set()
    decrease = set()
    for i in range(0, len(report)-1):
        if report[i+1] > report[i]:
            is_decreasing = False
            increase.add(report[i+1] - report[i])
        elif report[i+1] < report[i]:
            is_increasing = False
            decrease.add(report[i] - report[i+1])
        else:
            return False
    if is_increasing and not is_decreasing:
        increase.discard(1)
        increase.discard(2)
        increase.discard(3)
        if len(increase) == 0:
            return True
    elif is_decreasing and not is_increasing:
        decrease.discard(1)
        decrease.discard(2)
        decrease.discard(3)
        if len(decrease) == 0:
            return True
    return False

def solve2(L: list[list[int]]):
    sum = 0
    for report in L:
        if is_safe1(report):
            sum+=1
        else:
            for i in range(len(report)):
                sub_report = report.copy()
                sub_report.pop(i)
                if is_safe1(sub_report):
                    sum += 1
                    break
    return sum

        

    
L = read()
print(solve2(L))


