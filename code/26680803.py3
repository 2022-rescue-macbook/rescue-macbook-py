import sys

class node:
    def __init__(self, key):
        self.key = key
        self.mark = None

for _ in range(int(input())):
    n, tar = map(int, input().split())
    data = list(map(int, sys.stdin.readline().split()))
    d = list(map(lambda x: node(x), data))
    d[tar].mark = True
    seq = sorted(data, reverse=True)
    res, s_flag, u = 1, 0, d[0]
    while not u.mark or seq[s_flag] != u.key:
        if u.key == seq[s_flag]:
            res += 1
            s_flag += 1
        else:
            d.append(u)
        del d[0]
        u = d[0]
    print(res)