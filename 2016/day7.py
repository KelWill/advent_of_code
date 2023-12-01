import os
script_dir = os.path.dirname(__file__)


def supports(s):
    within_brackets = False
    has_abba = False
    for i, x in enumerate(s):
        if i >= len(s) - 3:
            return has_abba
        if x == "[":
            within_brackets = True
        elif x == "]":
            within_brackets = False
        elif s[i] != s[i + 1] and s[i + 1] == s[i + 2] and s[i] == s[i + 3] and s[i + 1] != "[" and s[i + 1] != "]":
            if within_brackets:
                return False
            else:
                has_abba = True
    return has_abba


def supports_ssl(s):
    within_brackets = False
    aba = set()
    bab = set()
    for i, x in enumerate(s):
        if i + 2 >= len(s):
            continue
        if x == "[":
            within_brackets = True
        elif x == "]":
            within_brackets = False
        elif s[i] == s[i + 2] and s[i] != s[i + 1]:
            if within_brackets:
                aba.add(s[i:i + 3])
            else:
                bab.add(s[i + 1] + s[i] + s[i + 1])
    return len(aba.intersection(bab)) > 0


# supports TLS(abba outside square brackets).
print(supports_ssl("aba[bab]xyz"))

support_count = 0
for line in open(script_dir + "/7.input").read().split("\n"):
    if supports_ssl(line):
        support_count = support_count + 1
print(support_count)
