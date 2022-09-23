import sys
input = sys.stdin.readline

def order(ps, m):
    idx = list(range(len(ps)))
    count = 1
    while ps:
        if ps[0] == max(ps):
            outi, outv = idx.pop(0), ps.pop(0)
            if outi == m: return count
            count += 1
        else:
            ps.append(ps.pop(0))
            idx.append(idx.pop(0))

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ps = list(map(int, input().split()))
    print(order(ps, m))