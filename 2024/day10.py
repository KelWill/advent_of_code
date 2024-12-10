from collections import defaultdict
real = open("./day10.input").read()
ex = open("./day10.example").read()

def main (s):
    G = defaultdict(lambda: -1) | {r + c * 1j: int(char) for r, row in enumerate(s.split("\n")) for c, char in enumerate(row) }
    result = []
    todo = [(p, p) for p, e in G.items() if e == 0]
    while todo:
        p, start = todo.pop()
        if G[p] == 9:
            result.append((start, p))
        todo += [(p + d, start) for d in (-1, 1, 1j, -1j) if G[p + d] == G[p] + 1]

    return len(set(result)), len(result)

print(main(ex), main(real))