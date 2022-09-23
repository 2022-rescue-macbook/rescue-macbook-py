import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,K = list(map(int,input().split()))
    seq=list(map(int,input().split()))
    index=[i for i in range(len(seq))]
    count={}
    for i in range(1,10):
        count[i]=0
    for i in seq:
        if i not in count: count[i]=0
        count[i]+=1
        
    top=max(seq)
    queue=[]
    head=0
    tail=0
    dead=[]
    popcount=0
    while True:
        if seq[head]==top: # pop!
            count[top]-=1
            popcount+=1
            if index[head]==K:
                sys.stdout.write(str(popcount)+'\n')
                break
            while count[top]==0 and top!=1: 
                top-=1
                
                
        else:
            tail+=1
            seq.append(seq[head])
            index.append(index[head])
        head+=1
