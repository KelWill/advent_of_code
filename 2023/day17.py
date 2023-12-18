import heapq

real = open("./day17.input").read()

ex = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


def main(s, min_moves=4, max_moves=10):
    ll = s.split("\n")
    positions = {(r, c): int(ll[r][c])
                 for r in range(len(ll)) for c in range(len(ll[r]))}
    MAX_R, MAX_C = max(positions)
    seen = set()
    todo = [(positions[(0, 1)], (0, 1), ((0, 1),)),
            (positions[(1, 0)], (1, 0), ((1, 0),))]
    while todo:
        curr = heapq.heappop(todo)
        cost, pos, prev_moves = curr
        r, c = pos
        if pos == (MAX_R, MAX_C):
            return cost

        left_right = [
            (1, 0), (-1, 0)] if prev_moves[-1][1] else [(0, 1), (0, -1)]
        same = [prev_moves[-1]]

        if len(prev_moves) < min_moves:
            possible_next_directions = same
        elif len(prev_moves) < max_moves:
            possible_next_directions = left_right + same
        else:
            possible_next_directions = left_right

        for dr, dc in possible_next_directions:
            next_pos = r + dr, c + dc
            if (dr, dc) == prev_moves[0]:
                next_prev_moves = prev_moves + ((dr, dc),)
            else:
                next_prev_moves = ((dr, dc),)
            if next_pos not in positions or (next_pos, next_prev_moves) in seen:
                continue
            heapq.heappush(
                todo, (cost + positions[next_pos], next_pos, next_prev_moves))
            seen.add((next_pos, next_prev_moves))


print("ex part 1", main(ex, min_moves=0, max_moves=3))
print("ex part 2", main(ex, min_moves=4, max_moves=10))
print("real part 1", main(real, min_moves=0, max_moves=3))
print("real part 2", main(real, min_moves=4, max_moves=10))
