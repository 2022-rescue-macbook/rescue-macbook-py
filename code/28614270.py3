
import sys
n=int(sys.stdin.readline())
for _ in range(n):
    n,m=map(int,sys.stdin.readline().split())
    importance=list(map(int,sys.stdin.readline().split()))
    new=sorted(importance,reverse=True)
    num=0
    idx=[]
    for i in range(len(importance)):
        idx.append(i)
    while len(importance)!=0:
        if importance[0]!=new[0] and len(new)!=1:
            a=importance.pop(0)
            importance.append(a)
            b=idx.pop(0)
            idx.append(b)
        else:
            num+=1
            if idx[0]==m:
                print(num)
                break
            del importance[0]
            del new[0]
            del idx[0]