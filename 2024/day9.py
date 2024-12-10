ex = """2333133121414131402"""
real = open("./day9.input").read()
from collections import defaultdict

def p1brutestupid (s):
    blocks = []
    for i, n in enumerate(s):
        if not i % 2:
            for j in range(int(n)):
                blocks.append(i // 2)
        else:
            for i in range(int(n)):
                blocks.append(".")
    while "." in blocks:
        i = blocks.index(".")
        blocks[i] = blocks.pop()
        while blocks[-1] == ".":
            blocks.pop()
        
    return sum(f * i for i, f in enumerate(blocks))

def render_ll (curr):
    line = ""
    while curr:
        line += str(curr["id"]) * curr["n"]
        line += "." * curr["space"]
        curr = curr["next"]
    return line

def p2 (s):
    head = {}
    curr = head
    for i, n in enumerate(s):
        if i % 2 == 0:
            curr["next"] = { "n": int(n), "id": i // 2, "space": 0, "next": None }
            curr["next"]["prev"] = curr
            curr = curr["next"]
        else:
            curr["space"] = int(n)

    head = head["next"]
    todo = []
    curr = head

    while curr:
        todo.append(curr)
        curr = curr["next"]

    l = render_ll(head)

    while todo:
        me = todo.pop()
        curr = head
        found = 0
        while curr != me:
            space = curr["space"]
            if me["n"] > space:
                curr = curr["next"]
                continue
            if curr["next"] == me:
                curr["space"] = 0
                me["space"] = space + me["space"]
                break

            curr["space"] = 0
            next = curr["next"]

            me_prev = me["prev"]
            me_next = me["next"]
            me["prev"]["next"] = me["next"]
            if me_next:
                me_next["prev"] = me_prev
            me_prev["space"] += me["space"] + me["n"]

            me["prev"] = curr
            me["next"] = next

            curr["next"] = me
            next["prev"] = me

            me["space"] = space - me["n"]
            break
        if found > 1:
            raise Exception("uh oh")


    checksum = 0
    position = 0
    curr = head
    while curr:
        for j in range(position, curr["n"] + position):
            checksum += curr["id"] * (j)
        position += curr["n"] + curr["space"]
        curr = curr["next"]

    return checksum
    

print(p2(ex))
print(p2(real))

