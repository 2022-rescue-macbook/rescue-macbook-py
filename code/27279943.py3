t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    pos=list(map(int,input().split()))
    idx=list(range(n))
    idx[m]='target'
    index=0
    while True:    
        if pos[0]==max(pos):
            index+=1
            if idx[0]=='target':
                print(index)
                break
            else:
                pos.pop(0)
                idx.pop(0)
        else:
            pos.append(pos.pop(0))
            idx.append(idx.pop(0))        
