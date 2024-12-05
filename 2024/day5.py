input = open(0).read()
rule_string, pages_string = input.split("\n\n")
from collections import defaultdict
rules = defaultdict(set)
for rule in rule_string.split("\n"):
    before, after = rule.split("|")
    rules[before].add(after)

def find_valid_order (page):
    for c in page.keys():
        for after in rules[c]:
            if after in page and page[after] < page[c]:
                page[after], page[c] = page[c], page[after]
                return find_valid_order(page)
    return page

p1 = 0
p2 = 0
for line in pages_string.split("\n"):
    page = { c : i for i, c in enumerate(line.split(","))}
    valid = True
    for c in page.keys():
        if any(after in page and page[after] < page[c]):
            valid = False
    if valid:
        p1 += int(line.split(",")[len(page) // 2])
    if not valid:
        page = find_valid_order(page)
        mid = len(page) // 2
        for p in page.keys():
            if page[p] == mid:
                p2 += int(p)
                break

print(p1, p2)



