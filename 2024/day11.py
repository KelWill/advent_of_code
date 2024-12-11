ex = "125 17"
real = "2 77706 5847 9258441 0 741 883933 12"

def blink (stone):
    if not stone:
        return [1]
    
    if len(str(stone)) % 2:
        return [2024 * stone]
    
    stone = str(stone)
    l = stone[:len(stone) // 2]
    r = stone[len(stone) // 2:]

    return [int(l), int(r)]


def main (s):
    stones = [*map(int, s.split())]

    def inner (stone, moves, dp):
        if (stone, moves) in dp:
            return dp[(stone, moves)]
        if moves == 0:
            return 1
        
        dp[(stone, moves)] = sum(inner(b, moves - 1, dp) for b in blink(stone))
        return dp[(stone, moves)]

    p1, p2 = {}, {}
    return sum(inner(stone, 25, p1) for stone in stones), sum(inner(stone, 75, p2) for stone in stones)

print(main(ex), main(real))

