class LL:
    def __init__(self, v):
        self.v = v
        self.next = None
        self.prev = None

def get_list_from_zero (lls):
    zero = None
    for ll in lls:
        if ll.v == 0:
            zero = ll

    results = []
    curr = zero
    while len(results) < len(lls):
        results.append(curr.v)
        curr = curr.next
    return results

def move_backward (ll, lls):
    curr = ll

    for _i in range(abs(ll.v) % len(lls)):
        curr = curr.prev

    # remove ll from list
    ll.prev.next = ll.next
    ll.next.prev = ll.prev

    prev = curr.prev
    curr.prev = ll
    ll.prev = prev
    prev.next = ll
    ll.next = curr


def move_forward (ll, lls):
    next_pos = ll

    for _i in range(ll.v % len(lls)):
        next_pos = next_pos.next

    # remove ll from list
    ll.prev.next = ll.next
    ll.next.prev = ll.prev

    next = next_pos.next
    next_pos.next = ll
    ll.next = next
    ll.prev = next_pos
    next.prev = ll

def solve(input):
    numbers = list(map(int, input.split("\n")))

    lls = [LL(n) for n in numbers]
    for i in range(len(lls)):
        lls[i].prev = lls[i - 1]
        lls[i].next = lls[(i + 1) % len(lls)]
    
    for ll in lls:
        if ll.v == 0: continue
        elif ll.v > 0: move_forward(ll, lls)
        else: move_backward(ll, lls)

    ordered_list = get_list_from_zero(lls)

    return sum(ordered_list[n % len(ordered_list)] for n in [1000, 2000, 3000])

print(solve(open("./20.example").read()))
print(solve(open("./20.input").read()))
