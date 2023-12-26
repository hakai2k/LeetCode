def cookies(g, s):
    g.sort()
    s.sort()
    success = 0
    i = j = 0
    while j < len(s) and i < len(g):
        if g[i] <= s[j]:
            success = success + 1
            i = i + 1
        j = j + 1
    return success

g = [1,2]
s = [1,2,3]

print(cookies(g,s))