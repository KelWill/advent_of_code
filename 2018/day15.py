import math

ex = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

ex2 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

ex3 = """#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########"""

ex4 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""

ex5 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""


def main(s, elf_attack=3):
    walls = set()
    board = set()
    goblins = {}
    elves = {}
    for r, row in enumerate(s.split("\n")):
        for c, char in enumerate(row):
            if char == "#":
                walls.add((r, c))
            elif char == "G":
                goblins[(r, c)] = [200, 3]
            elif char == "E":
                elves[(r, c)] = [200, elf_attack]
            board.add((r, c))
    R = r
    C = c
    original_elf_count = len(elves)

    DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def paths_to_points(start, targets):
        seen = set()
        paths = [[(start)]]
        unavailable_locations = (walls | elves.keys() | goblins.keys())
        while paths:
            next_paths = []
            for path in paths:
                r, c = path[-1]
                seen.add((r, c))
                for dr, dc in DIRECTIONS:
                    rr = r + dr
                    cc = c + dc
                    if not (rr, cc) in board:
                        continue
                    if (rr, cc) in seen:
                        continue
                    if (rr, cc) in unavailable_locations:
                        continue
                    seen.add((rr, cc))
                    next_paths.append(path + [(rr, cc)])
            next_paths.sort(key=lambda x: x[-1])
            for path in next_paths:
                (r, c) = path[-1]
                if (r, c) in targets:
                    return path
            paths = next_paths
        return None

    def available_attack_points(creatures):
        results = []
        unavailable_locations = walls | elves.keys() | goblins.keys()
        for (r, c) in creatures:
            for dr, dc in DIRECTIONS:
                rr = r + dr
                cc = c + dc
                if not (rr, cc) in unavailable_locations:
                    results.append((rr, cc))
        return set(results)

    def attack_enemy(creature, loc, enemies):
        (r, c) = loc
        potential_enemies = []
        for (dr, dc) in DIRECTIONS:
            rr = r + dr
            cc = c + dc
            if (rr, cc) in enemies:
                potential_enemies.append((rr, cc, enemies[(rr, cc)]))

        if not potential_enemies:
            return

        min_health = min(enemy[0] for r, c, enemy in potential_enemies)
        potential_enemies = [
            (r, c, enemy) for r, c, enemy in potential_enemies if enemy[0] == min_health]
        potential_enemies = sorted(potential_enemies)
        r, c, enemy = potential_enemies[0]
        enemy[0] -= creature[1]
        if enemy[0] <= 0:
            del enemies[(r, c)]

    def stringify():
        board = []
        for r in range(R + 1):
            row = ""
            for c in range(C + 1):
                char = "."
                if (r, c) in walls:
                    char = "#"
                elif (r, c) in goblins:
                    char = "G"
                elif (r, c) in elves:
                    char = "E"
                row += char
            board.append(row)
        return "\n".join(board)

    def is_next_to_enemy(loc, enemies):
        r, c = loc
        for dr, dc in DIRECTIONS:
            if (r + dr, c + dc) in enemies:
                return True
        return False

    def creature_turn(loc, creatures, enemies):
        r, c = loc
        creature = creatures[(r, c)]

        if is_next_to_enemy(loc, enemies):
            attack_enemy(creature, loc, enemies)
            return loc
        else:
            attack_points = available_attack_points(enemies)
            attack_path = paths_to_points((r, c), attack_points)
            if attack_path:
                move = attack_path[1]
                del creatures[(r, c)]
                creatures[move] = creature
                attack_enemy(creature, move, enemies)
                return move
        return (r, c)

    def game_turn():

        gone = set()
        for r in range(R + 1):
            for c in range(C + 1):
                if (r, c) in gone:
                    continue
                move = (r, c)
                if (r, c) in elves:
                    move = creature_turn((r, c), elves, goblins)
                elif (r, c) in goblins:
                    move = creature_turn((r, c), goblins, elves)
                gone.add(move)
    turn_count = -1
    while goblins and elves:
        game_turn()
        turn_count += 1
    print(stringify())

    creatures = elves | goblins
    hp = sum(
        [(creatures)[creature][0] for creature in creatures])

    winner = "elves" if elves else "goblins"
    print(f"winner {winner} turn_count: {turn_count}, hp: {hp}")
    dead_elf_count = original_elf_count - len(elves)
    return (winner, dead_elf_count == 0, (turn_count + 1) * hp)


# print(main(ex3))
print(main(ex), "Outcome: 37 * 982 = 36334")
print(main(ex2), "Outcome: 46 * 859 = 39514")
print(main(ex4), "Outcome: 20 * 937 = 18740")
print(main(ex5), "Outcome: 54 * 536 = 28944")

print(main(open("day15.input").read()), "Outcome: 183300")

input = open("day15.input").read()
for attack in range(4, 201):
    winner, no_dead_elves, result = main(input, attack)
    if winner == "elves" and no_dead_elves:
        print(attack, result)
        break


"""
## bug list

- missed attack stage after refactoring code
- didn't have correct order for directions for reading order
- didn't change an 'elves' to 'creatures' after refactoring code
- had two loops and renamed outer loop variable in inner loop thinking it'd be safe
- summed location rather than hit points because wasn't iterating what I thought I was iterating
- was incorrectly early returning first found valid location rather than best possible location
- misread instructions—that goal was for elves to win, not for no dead elves
"""
