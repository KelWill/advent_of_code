
import os


def has_abba(s):
    for i in range(0, len(s) - 3):
        if s[i] == s[i + 3] and s[i] != s[i + 1] and s[i + 1] == s[i + 2]:
            return True
    return False


def supports_abba(s):
    parts = s.replace(']', '[').split('[')
    parts_in_brackets = [p for i, p in enumerate(parts) if i % 2 == 1]
    parts_not_in_brackets = [p for i, p in enumerate(parts) if i % 2 == 0]

    for p in parts_in_brackets:
        if has_abba(p):
            return False

    for p in parts_not_in_brackets:
        if has_abba(p):
            return True

    return False


def supports_ssl(s):
    parts = s.replace(']', '[').split('[')
    parts_in_brackets = [p for i, p in enumerate(parts) if i % 2 == 1]
    parts_not_in_brackets = [p for i, p in enumerate(parts) if i % 2 == 0]

    abas = set()
    for p in parts_in_brackets:
        for i in range(0, len(p) - 2):
            if p[i] == p[i + 1]:
                continue
            if p[i] == p[i + 2]:
                abas.add(p[i + 1] + p[i] + p[i + 1])
    for p in parts_not_in_brackets:
        for i in range(0, len(p) - 2):
            s = p[i:i + 3]
            if s in abas:
                return True

    return False


script_dir = os.path.dirname(__file__)
support_count = 0
for line in open(script_dir + "/7.input").read().split("\n"):
    if supports_ssl(line):
        support_count = support_count + 1
print(support_count)
