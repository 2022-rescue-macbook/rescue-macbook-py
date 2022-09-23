from bisect import bisect_left
for _ in range(int(input())):
    n,m=map(int,input().split())
    inp=list(map(int,input().split()))
    idx=[[] for _ in range(10)]
    for i in range(n):
        idx[inp[i]].append(i)
    cur=0
    cnt=1
    for i in range(9,inp[m],-1):
        if len(idx[i])==0:
            continue
        cnt+=len(idx[i])
        cur=idx[i][bisect_left(idx[i],cur)-1]
    temp=bisect_left(idx[inp[m]],m)-bisect_left(idx[inp[m]],cur)
    if temp<0:
        temp+=len(idx[inp[m]])
    print(cnt+temp)