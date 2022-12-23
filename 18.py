example_input = open("18.example").read()
real_input = open("18.input").read()

def solve_p1(input):
    grid = set()

    for row in input.split("\n"):
        grid.add(tuple(map(int, row.split(","))))
    
    count = 0
    for (x, y, z) in grid:
        for (xx, yy, zz) in ((x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)):
            if (xx, yy, zz) not in grid:
                count += 1
    return count

def solve_p2(input):
    grid = set()

    for row in input.split("\n"):
        grid.add(tuple(map(int, row.split(","))))

    dimension_cube = [[-1e9, 1e9], [-1e9, 1e9], [-1e9, 1e9]]
    for r in grid:
        for dim in range(3):
            dimension_cube[dim][0] = max(r[dim], dimension_cube[dim][0])
            dimension_cube[dim][1] = min(r[dim], dimension_cube[dim][1])

    internal = set()
    external = set()

    def is_airpocket (grid, dimension_cube, pos):
        nonlocal internal
        nonlocal external
        todo = [pos]
        visited = set()
        visited.add(pos)
        result = True

        while todo:
            pos = todo.pop()
            (x, y, z) = pos

            if pos in internal:
                return True
            if pos in external:
                return False

            in_range = all(dimension_cube[dim][1] <= pos[dim] <= dimension_cube[dim][0] for dim in range(3))
            if not in_range:
                result = False
                break

            for n in ((x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)):
                if n in grid: continue
                if n in visited: continue
                visited.add(n)
                todo.append(n)

        for n in visited:
            (internal if result else external).add(n)
        return result

    count = 0
    for (x, y, z) in grid:
        for pos in ((x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)):
            if pos not in grid and not is_airpocket(grid, dimension_cube, pos):
                count += 1

    return count


print(solve_p2(example_input))
print(solve_p2(real_input))
