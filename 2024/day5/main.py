from page import Page
from functools import cmp_to_key

with open("day5/input.txt", "r") as f:
    content = f.readlines()

def parse_page(line: str):
    before, after = line.strip().split("|")
    before = Page.get(int(before))
    after = Page.get(int(after))
    before.pages_after.add(after)
    after.pages_before.add(before)

sum = 0
sum2 = 0

for line in content:
    if "|" in line:
        parse_page(line)
    elif "," in line:
        printing = line.strip().split(",")
        printing = [Page.get(int(x)) for x in printing]
        is_good_printing = True
        for i, page in enumerate(printing):
           pages_before = printing[0:i]
           pages_after = printing[i+1:]
           if not page.is_good_printing(pages_before, pages_after):
               is_good_printing = False
               break
        if is_good_printing:
            middle = printing[len(printing)//2]
            sum += middle.number
        else:
            new_printing = printing.copy()
            def comp(a: Page, b: Page):
                if b in a.pages_after:
                    return -1
                elif a in b.pages_after:
                    return 1
                return 0
            new_printing.sort(key=cmp_to_key(comp))
            middle = new_printing[len(printing)//2]
            sum2+=middle.number

print(sum, sum2)