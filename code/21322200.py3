num_t = int(input()) # the number of tc

for t in range(num_t):
    n, m = list(map(int,input().split(' '))) # N. M
    pr = list(map(int,input().split(' '))) # priority
    idx = [i for i in range(n)]
    x = 0 # order
    
    while len(pr):
        if pr[0]==max(pr):
            x+=1
            pr.pop(0)
            if idx.pop(0)==m:
                print(x)
                break
        else:
            pr.append(pr.pop(0))
            idx.append(idx.pop(0))