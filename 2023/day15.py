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
    boxes = [([], []) for _x in range(256)]
    part1score = sum(hash(line) for line in s.split(","))
    for line in s.split(","):
        if "-" in line:
            label = line.split("-")[0]
            box_number = hash(label)
            labels, focal_lengths = boxes[box_number]
            if label in labels:
                i = labels.index(label)
                labels.pop(i)
                focal_lengths.pop(i)
        elif "=" in line:
            label, r = line.split("=")
            focal_length = int(r)
            box_number = hash(label)
            labels, focal_lengths = boxes[box_number]
            if label in labels:
                focal_lengths[labels.index(label)] = focal_length
            else:
                labels.append(label)
                focal_lengths.append(focal_length)
        else:
            raise Exception(f"unknown {line}")

    part2score = sum((i + 1) * (b + 1) * boxes[i][1][b] for i in range(len(boxes))
                     for b in range(len(boxes[i][1])))
    return part1score, part2score


print(
    "ex:", main(ex),
    "real:", main(real)
)
