n = int(input())

for _ in range(n):
    n,m = map(int,input().split())
    imp = list(map(int,input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'
    
    sol = 0
    
    while True:
        if imp[0] != max(imp):
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
        else:
            sol += 1
            if idx[0] == 'target':
                print(sol)
                break
            else:
                idx.pop(0)
                imp.pop(0)
        
        
        
        