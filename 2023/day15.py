ex = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
real = open('./day15.input').read()


def hash(code):
    curr = 0
    for c in code:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr


def main(s):
    boxes = [dict() for _x in range(256)]
    part1score = sum(hash(line) for line in s.split(","))
    for line in s.split(","):
        match line.replace("-", "=").split("="):
            case [label, ""]:
                boxes[hash(label)].pop(label, None)
            case [label, focal_length]:
                boxes[hash(label)][label] = int(focal_length)

    part2score = sum((box_i + 1) * (lense_i + 1) * focal_length for box_i, box in enumerate(boxes)
                     for lense_i, focal_length in enumerate(box.values()))
    return part1score, part2score


print(
    "ex:", main(ex),
    "real:", main(real)
)
