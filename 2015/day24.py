# all groups need to weigh the same
# fewest number of packages in group 1
# minimize product of weights

from itertools import combinations


def prod(nums):
    product = 1
    for x in nums:
        product = product * x
    return product


def main(weights):
    weights = [int(w) for w in weights.split("\n")]
    goal_weight = int(sum(weights) / 4)
    solutions = []
    for i in range(1, len(weights)):
        for p in combinations(weights, i):
            if sum(p) != goal_weight:
                continue
            rest = [w for w in weights if not w in p]
            has_solution = False
            for j in range(1, len(rest)):
                for q in combinations(rest, j):
                    if sum(q) != goal_weight:
                        continue
                    rest_rest = [r for r in rest if r not in q]
                    for k in range(1, len(rest_rest)):
                        for s in combinations(rest_rest, k):
                            if sum(s) != goal_weight:
                                continue
                            has_solution = True
                            break
                    if has_solution:
                        break
                if has_solution:
                    break

            if has_solution:
                solutions.append(p)
        if len(solutions):
            break
    print(solutions)
    return min(prod(sol) for sol in solutions)

    # def main(weights):
    #     print(weights)
    # weights = [int(w) for w in weights.split("\n")]
    # goal_weight = int(sum(weights) / 3)

    #     results = []
    #     dp(weights, [], [], [], goal_weight, results)
    #     print(results)

    #     min_a = min(len(result[0]) for result in results)
    #     possible_results = [
    #         result[0] for result in results if len(result[0]) == min_a
    #     ]
    #     m = None
    #     for x in possible_results:
    #         p = 1
    #         for a in x:
    #             p = p * a
    #         if p < m:
    #             p = m

    #     return m

    # def dp(weights, a, b, c, goal, results):
    #     sum_a = sum(a)
    #     sum_b = sum(b)
    #     sum_c = sum(c)
    #     print(a, b, c, goal)
    #     if sum_a == goal and sum_b == goal and sum_c == goal:
    #         results.append([a, b, c])

    #     for to_add in weights:
    #         updated_weights = [w for w in weights if w != to_add]
    #         if sum_a + to_add <= goal:
    #             dp(updated_weights, a + [to_add], b, c, goal, results)
    #         if sum_b + to_add <= goal:
    #             dp(updated_weights, a, b + [to_add], c, goal, results)
    #         if sum_c + to_add <= goal:
    #             dp(updated_weights, a, b, c + [to_add], goal, results)


ex = """1
2
3
4
5
7
8
9
10
11"""
real = """1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113"""
print(main(ex))
print(main(real))
