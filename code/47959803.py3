from sys import stdin

cases = int(stdin.readline().strip())
for _ in range(cases):
    N,M = map(int,stdin.readline().strip().split())
    docu = tuple(map(int,stdin.readline().strip().split()))
    target = sorted(set([i for i in set(docu) if i>=docu[M]]),reverse=True)
    orders = [None]*N
    order = 1
    last = 0
    tmp = 0
    
    for i in target:
        for j in range(last,N):
            if docu[j] == i:
                orders[j] = order
                order += 1
                tmp = j
                
        for j in range(0,last):
            if docu[j] == i:
                orders[j] = order
                order += 1
                tmp = j

        last = tmp
    
    print(orders[M])