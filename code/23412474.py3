import sys
rep=int(sys.stdin.readline())
for loop in range(rep):
    n,m=list(map(int,sys.stdin.readline().split()))
    queue=list(map(int,sys.stdin.readline().split()))
    ans,targetPri=1,queue[m]
    count={9:0,8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0}
    for x in queue: count[x]+=1
    for p in count:
        if count[p]>0:
            maxPri=p
            break
    for p in count:
        if p==targetPri: break
        ans+=count[p]
    lastIdx=n-1
    if maxPri==targetPri: lastIdx-=1
    while maxPri>targetPri:
        for i in range(lastIdx,lastIdx-n,-1):
            if queue[i%n]==maxPri:
                lastIdx=(i-1)%n
                break
        for i in range(maxPri-1,0,-1):
            if count[i]>0:
                maxPri=i
                break
    for i in range(lastIdx+2,lastIdx+n+2):
        if i%n==m:break
        if queue[i%n]==targetPri: ans+=1
    print(ans)