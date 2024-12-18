from collections import defaultdict
import heapq
import random

def path_to_exit (nums, R, C):
    M = defaultdict(lambda: "#") | { x + y * 1j: "." for y in range(R + 1) for x in range(C + 1) }
    i = 0
    for pos in nums:
        M[pos] = "#"
    seen = set()
    exit = C + R * 1j
    todos = [(0, 0, 0, [])]
    while todos:
        dist, _r, curr, path = heapq.heappop(todos)
        if curr == exit:
            return path
        for d in (1, -1, 1j, -1j):
            if M[curr + d] == "#" or (curr + d) in seen:
                continue
            heapq.heappush(todos, (dist + 1, random.random(), curr + d, path + [curr + d]))
            seen.add(curr + d)

def main (s, R, C, p1bytes):
    nums = []
    for l in s.split("\n"):
        x, y = [*map(int, l.split(","))]
        nums.append(x + y * 1j)

    p1 = len(path_to_exit(nums[:p1bytes], R, C))
    i = p1bytes
    while True:
        nodes = path_to_exit(nums[:i + 1], R, C)
        if not nodes:
            return p1, nums[i]
        while nums[i] not in nodes:
            i += 1

print(main(open("./day18.example").read(), 6, 6, 12))
print(main(open("./day18.input").read(), 70, 70, 1024))




