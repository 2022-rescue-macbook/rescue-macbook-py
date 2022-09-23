t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    c=1
    imp=[[i for i in range(n)],list(map(int,input().split()))]
    while len(imp)>0:
        if imp[1][0]!=max(imp[1]):
            imp[0].append(imp[0][0])
            imp[1].append(imp[1][0])
            imp[0].remove(imp[0][0])
            imp[1].remove(imp[1][0])
        else:
            if imp[0][0]==m:
                print(c)
                break
            imp[0].remove(imp[0][0])
            imp[1].remove(imp[1][0])
            c+=1