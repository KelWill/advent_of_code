import math

def presents_received (n):
    divisors = get_divisors(n)
    return sum([11 * n for n in divisors][-50:])

def get_divisors (n):
    divs = set()
    divs.add(n)
    small_divisors = [x for x in range(1, int(math.sqrt(n)) + 1) if n % x == 0]
    large_divisors = [n/x for x in small_divisors if x != n /x]
    return small_divisors + large_divisors

goal = 36000000

counts = [0 for _elf in range(1, int(goal / 10) + 1)]

for elf in range(1, int(goal / 10) + 1):
    for x in range(1, 51):
        if x * elf >= len(counts):
            break
        counts[x * elf] = counts[x * elf] + elf * 11

for i, f in enumerate(counts):
    if f >= goal:
        print(i, f)
        break

# 3534300 36012670