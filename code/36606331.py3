import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    i,j = map(int,input().split())
    ranks = list(map(int,input().split()))
    idx = list(range(i))
    idx[j] = -1
    order = 0
    while True:
        if ranks[0] == max(ranks):
            order += 1
            
            if idx[0] == -1:
                print(order)
                break
            else:
                ranks.pop(0)
                idx.pop(0)
        else:
            ranks.append(ranks.pop(0))
            idx.append(idx.pop(0))
    