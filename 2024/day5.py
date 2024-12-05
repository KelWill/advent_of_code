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

result = [0, 0]
for line in pages_string.split("\n"):
    page = { c : i for i, c in enumerate(line.split(","))}
    pre_order_list = sorted(page.keys(), key=lambda c: page[c])
    page = find_valid_order(page)
    post_order_list = sorted(page.keys(), key=lambda c: page[c])
    result[pre_order_list == post_order_list] += int(post_order_list[len(post_order_list) // 2])

print(*result)
