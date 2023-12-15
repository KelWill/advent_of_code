ex = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
real = open('./day15.input').read()


def hash(code):
    curr = 0
    for c in code:
        curr = ((curr + ord(c)) * 17) % 256
    return curr


def main(s):
    boxes = [{} for _x in range(256)]
    for line in s.split(","):
        if "-" in line:
            label = line.strip("-")
            boxes[hash(label)].pop(label, None)
        else:
            label, focal_length = line.split("=")
            boxes[hash(label)][label] = int(focal_length)

    part2score = sum(box_i * lense_i * focal_length for box_i, box in enumerate(boxes, start=1)
                     for lense_i, focal_length in enumerate(box.values(), start=1))
    part1score = sum(hash(line) for line in s.split(","))
    return part1score, part2score


print(
    "ex:", main(ex),
    "real:", main(real)
)
