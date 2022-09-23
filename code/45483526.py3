import sys
T = int(sys.stdin.readline().split()[0])
for _ in range(T):
    N,M = map(int, sys.stdin.readline().split())
    imprt = list(map(int, sys.stdin.readline().split()))
    target = [0 for i in range(N)]
    target[M] = 1
    
    order = 1
    while True:
        if imprt[0] == max(imprt):
            del imprt[0]
            removed = target.pop(0)
            if removed==1:
                break
            else:
                order+=1
        else:
            imprt.append(imprt.pop(0))
            target.append(target.pop(0))
    print(order)