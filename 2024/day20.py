from collections import Counter, defaultdict


ex = open("./day20.example").read()
real = open("./day20.input").read()


def main (s, cheat_seconds, goal_seconds):
    M = defaultdict(lambda: "#") | { r * 1j + c: char for r, row in enumerate(s.splitlines()) for c, char in enumerate(row) }
    start = next(pos for pos, char in M.items() if char == "S")
    end = next(pos for pos, char in M.items() if char == "E")

    dirs = (1, -1, 1j, -1j)
    dists = {}
    todo = [start]
    dist = 0
    while todo:
        next_todo = []
        for t in todo:
            dists[t] = dist
            for d in dirs:
                if t + d in dists or M[t + d] == "#":
                    continue
                next_todo.append(t + d)
        todo = next_todo
        dist += 1
    
    seen = set()
    cheats = dict()
    for pos, dist in dists.items():
        todo = [pos]
        for i in range(cheat_seconds):
            nexts = []
            for t in todo:
                for d in dirs:
                    if (pos, t + d) in seen:
                        continue
                    seen.add((pos, t + d))
                    if t + d in dists:
                        saved_time = dists[t + d] - dist - i - 1
                        if saved_time >= goal_seconds:
                            cheats[(pos, t + d)] = saved_time
                    nexts.append(t + d)
            todo = nexts

    print(Counter(sorted(cheats.values())))
    return len(cheats)




print(main(ex, 20, 50))
# print(main(real, 20, 100))
