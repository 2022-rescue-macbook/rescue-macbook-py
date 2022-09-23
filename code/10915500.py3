from sys import stdin
for i in range(int(stdin.readline())):
    n,m=map(int,stdin.readline().split())
    l=list(map(int,stdin.readline().split()))
    nl=sorted(l,reverse=True)
    imp=l[m]
    del(l[m])
    l.insert(m,'X')
    result=0
    idx=0
    result=0
    pl=[]
    if n==1:
        result=1
    else:
        while len(pl)!=n:
            if l[idx]==nl[0]:
                del(l[idx])
                del(nl[0])
                if idx==0:
                    idx=len(l)
                else:
                    idx-=1
                result+=1
            elif max(nl)==imp and l[idx]=='X':
                result+=1
                break
            if idx<len(l)-1:    
                idx+=1
            elif l==[]:
                break
            else:
                idx=0
    print(result)