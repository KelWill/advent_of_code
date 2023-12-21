from math import prod
import re


ex = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


def get_ints(s):
    return list(map(int, re.findall(r'\d+', s)))


def parse_rules(rule_string):
    res = {}
    for rule in rule_string.split("\n"):
        name, rest = rule.split("{")
        rest = rest.strip("}")

        res[name] = rest.split(",")
    return res


def part2(s):
    rules, _part_string = s.split("\n\n")
    rule_map = parse_rules(rules)

    todo = [('in', [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])]

    accepted = []
    while todo:
        node, ranges = todo.pop()
        print(node, ranges)
        if node == 'A':
            accepted.append((ranges))
            continue
        if node == 'R':
            continue

        rules = rule_map[node]

        for rule in rules:
            if '<' in rule:
                p, rest = rule.split('<')
                n, dest = rest.split(":")
                n = int(n)
                i = 'xmas'.index(p)
                start, end = ranges[i]
                if n < start:
                    continue
                l = (start, n - 1)
                r = (n, end)
                todo.append((dest, ranges[:i] + [l] + ranges[i + 1:]))
                ranges[i] = r
                n = int(n)

            elif '>' in rule:
                p, rest = rule.split('>')
                n, dest = rest.split(":")
                n = int(n)
                i = 'xmas'.index(p)
                start, end = ranges[i]
                if n > end:
                    continue
                l = (start, n)
                r = (n + 1, end)
                todo.append((dest, ranges[:i] + [r] + ranges[i + 1:]))
                ranges[i] = l
                n = int(n)
            else:
                todo.append((rule, ranges))

    total = 0
    for a in accepted:
        total += prod(end - start + 1 for start, end in a)
    return total


def part1(s):
    rules, part_string = s.split("\n\n")
    rules = parse_rules(rules)
    parts = []
    for p in part_string.split("\n"):
        parts.append(get_ints(p))
    part_order = 'xmas'
    accepted_parts = []
    for part in parts:
        curr = 'in'
        while curr != 'R' and curr != 'A':
            rs = rules[curr]
            for r in rs:
                if '<' in r:
                    p, rest = r.split('<')
                    n, dest = rest.split(":")

                    n = int(n)
                    if part[part_order.index(p)] < n:
                        curr = dest
                        break
                elif '>' in r:
                    p, rest = r.split('>')
                    n, dest = rest.split(":")

                    n = int(n)
                    if part[part_order.index(p)] > n:
                        curr = dest
                        break
                else:
                    curr = r
        if curr == 'A':
            accepted_parts.append(part)

    return sum(sum(a) for a in accepted_parts)


print('ex', part1(ex))
print('real', part1(open("./day19.input").read()))
print('ex', part2(ex))
print('real', part2(open("./day19.input").read()))
