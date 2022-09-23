case=int(input())
for i in range(case):
    rank=[]
    n,m=map(int,input().split())
    rank=list(map(int,input().split()))
    target=[0]*n
    target[m]='target'
    order=0
    while (1):
        if rank[0]==max(rank):
            order+=1
            if target[0]=='target':
                print(order)
                break
            else:
                rank.pop(0)
                target.pop(0)
        else:
            rank.append(rank.pop(0))
            target.append(target.pop(0))