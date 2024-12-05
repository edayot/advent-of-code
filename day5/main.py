from page import Page

with open("day5/input.txt", "r") as f:
    content = f.readlines()

def parse_page(line: str):
    before, after = line.strip().split("|")
    before = Page.get(int(before))
    after = Page.get(int(after))
    before.pages_after.add(after)
    after.pages_before.add(before)

sum = 0

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

print(sum)