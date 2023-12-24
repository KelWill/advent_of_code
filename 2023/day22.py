from collections import defaultdict
import pprint

real = open("./day22.input").read()
ex = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def xyz(s):
    return list(map(int, s.split(",")))


def main(s):
    bricks = []

    for i, l in enumerate(s.split("\n")):
        start, end = map(xyz, l.split("~"))
        bricks.append(((min(start[2], end[2]), max(start[2], end[2])), (min(start[0], end[0]), max(
            start[0], end[0])), (min(start[1], end[1]), max(start[1], end[1])), chr(ord("A") + i)))
    bricks.sort()
    stationary_bricks = {}

    while bricks:
        nxt_bricks = []
        for brick in bricks:
            falling = True
            if brick[0][0] == 1:
                stationary_bricks[brick] = {
                    "supported_by": set(),
                    "supporting": set()
                }
                falling = False
            nxt_stationary = {}
            for floor in stationary_bricks:
                if floor[0][1] != brick[0][0] - 1:
                    continue
                xintersect = len(
                    range(max(floor[1][0], brick[1][0]), min(floor[1][1], brick[1][1]) + 1))
                yintersect = len(
                    range(max(floor[2][0], brick[2][0]), min(floor[2][1], brick[2][1]) + 1))
                if not xintersect or not yintersect:
                    continue
                falling = False
                if not brick in nxt_stationary:
                    nxt_stationary[brick] = {
                        "supported_by": set([floor]),
                        "supporting": set()
                    }
                else:
                    nxt_stationary[brick]["supported_by"].add(floor)
                stationary_bricks[floor]["supporting"].add(brick)
            stationary_bricks = stationary_bricks | nxt_stationary
            if falling:
                nxt_bricks.append(
                    ((brick[0][0] - 1, brick[0][1] - 1), brick[1], brick[2], brick[3]))

        bricks = nxt_bricks

    required_bricks = set()
    for b in stationary_bricks:
        brick = stationary_bricks[b]
        if len(brick["supported_by"]) == 1:
            required_bricks |= brick["supported_by"]
    part1 = len(stationary_bricks.keys() - required_bricks)

    def calculate_would_fall(b):
        fallen = set([b])
        todo = list(stationary_bricks[b]["supporting"])
        while todo:
            brick = todo.pop(0)
            if not (stationary_bricks[brick]["supported_by"] - fallen):
                for x in stationary_bricks[brick]["supporting"]:
                    todo.append(x)
                fallen.add(brick)
        return len(fallen)

    part2 = sum(calculate_would_fall(b) - 1 for b in stationary_bricks)

    return part1, part2


print("ex", main(ex))
print("real", main(real), (457, 79122))
