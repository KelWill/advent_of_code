from hashlib import md5
from collections import defaultdict

salt = "ihaygndm"


def get_hashes():
    i = 0
    while True:
        hash = md5(f"{salt}{i}".encode("utf-8"))
        for j in range(2016):
            hash = md5(hash.hexdigest().encode("utf-8"))
        yield hash.hexdigest()
        i += 1


def part1():
    iterator = get_hashes()

    five_time_hashes = defaultdict(list)
    hashes = []

    def get_hash(i):
        while i > len(hashes) - 1000:
            h = next(iterator)
            hashes.append(h)
            for j in range(0, len(h) - 5 + 1):
                if len(set(h[j:j + 5])) == 1:
                    five_time_hashes[h[j]].append(len(hashes) - 1)

        return hashes[i]

    def get_first_three(hash):
        for i in range(0, len(hash) - 3 + 1):
            if len(set(hash[i:i + 3])) == 1:
                return hash[i]
        return False

    results = []
    i = 0
    while len(results) < 64:
        hash = get_hash(i)
        k = get_first_three(hash)
        if k and five_time_hashes[k] and any(j > i and j <= i + 1000 for j in five_time_hashes[k]):
            print(len(results), hash, i)
            results.append(hash)
        if len(results) == 64:
            return i
        i += 1


print(part1())
