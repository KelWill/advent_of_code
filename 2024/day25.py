def fits (key, lock):
    return not any(k + l > 7 for k,l in zip(key, lock))

def main (s):
    key_locks = [set(), set()]
    for block in s.split("\n\n"):
        key_locks[block[0] == "#"].add(tuple(col.count("#") for col in [*zip(*block.split("\n"))]))
    return sum(fits(key, lock) for lock in key_locks[0] for key in key_locks[1])

print(main(open("./day25.example").read()))
print(main(open("./day25.input").read()))
