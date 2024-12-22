import functools


@functools.cache
def step (secret):
    secret = secret ^ (secret * (2 ** 6))
    secret = secret % (2 ** 24)
    secret = secret ^ (secret // (2 ** 5))
    secret = secret % (2 ** 24)
    secret = secret ^ (secret * (2 ** 11))
    secret = secret % (2 ** 24)
    return secret

def main (s):
    p1 = 0
    price_list = []
    for n in map(int, s.splitlines()):
        prices = [int(str(n)[-1])]
        price_list.append(prices)
        for i in range(2000):
            n = step(n)
            prices.append(int(str(n)[-1]))
        p1 += n

    diffs_list = []
    for prices in price_list:
        diffs = {}
        diffs_list.append(diffs)
        for i in range(5, len(prices)):
            diff = ",".join(str(prices[j] - prices[j - 1]) for j in range(i - 4, i))
            if diff not in diffs:
                diffs[diff] = prices[i - 1]
    all_potential_diffs = set()
    for diff in diffs_list:
        all_potential_diffs |= set(diff.keys())

    p2 = 0
    for diff in all_potential_diffs:
        profit_at_diff = sum(d[diff] if diff in d else 0 for d in diffs_list)
        p2 = max(p2, profit_at_diff)
    return p1, p2

print(main("""1
2
3
2024"""))

print(main(open("./day22.input").read()))