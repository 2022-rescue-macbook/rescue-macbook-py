n = int(input())
for i in range(n):
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    x=[[k,i] for i,k in enumerate(x)]
    re=[]
    xs=sorted(x,key=lambda x: x[0])
    i=0
    while True:
        if re and re[-1][1] == b:
            break
        if x[i][0] == xs[a-1][0]:
            re.append(x[i])
            a-=1
        else:
            x.append(x[i])
        i+=1
    print(len(re))