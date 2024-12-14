import re
ex = open("./day13.example").read()
real = open("./day13.input").read()

def get_ints (s):
    return [*map(int, re.findall(r"\d+", s))]

def tokens_to_reach_prize (a, b, p):
    """
    A * ax + B * bx = px
    A * ay + B * by = py

    A = (px - B * bx) / ax
    (px - B * bx) * ay / ax + B * by = py
     -B * bx * ay /ax + B * by = py
     -B * bx * ay /ax + B * by = (py - px * ay/ax) / (-bx * ay/ax + by)
    """

    ax, ay = a
    bx, by = b
    px, py = p

    B = (py - px * ay/ax) / (-bx * ay/ax + by)
    A = (px - B * bx) / ax

    if px == round(A) * ax + round(B) * bx and py == round(A) * ay + round(B) * by and A >= 0 and B >= 0:
        return A * 3 + B
    
    return 0


def main(s):
    parts = s.split("\n\n")
    p1, p2 = 0, 0
    for p in parts:
        a, b, prizes = [*map(get_ints, p.split("\n"))]
        p1 += tokens_to_reach_prize(a, b, prizes)
        p2 += tokens_to_reach_prize(a, b, (prizes[0] + 10000000000000, prizes[1] + 10000000000000))
    return p1, p2

print(main(ex))
print(main(real)) # 33481.0
