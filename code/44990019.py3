a=int(input())
for n in range(a):
    im=list(map(int,input().split()))
    pr=list(map(int,input().split()))
    p=sorted(pr,reverse=True)
    tf=[1 for _ in range(len(p))]
    now, answer=0,1
    for i in p:
        while True:
            now%=im[0]
            if tf[now]==1 and pr[now]==i:
                if now==im[1]:print(answer)
                else: tf[now]=0
                answer+=1
                break
            now+=1
        if now==im[1]:break
