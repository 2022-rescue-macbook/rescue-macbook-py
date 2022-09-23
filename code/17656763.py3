t=int(input())
while t>0:
    n,m=map(int,input().split())
    que=list(map(int,input().split()))
    com=list(set(que))
    com.sort(reverse=True)
    cnt=0
    while m>=0:
        if que[0]==com[0]:
            del que[0]
            if que.count(com[0])==0:
                del com[0]
            cnt+=1
            m-=1
        elif m==0:
            que.append(que[0])
            del que[0]
            m=len(que)-1
        else:
            que.append(que[0])
            del que[0]
            m-=1
    print(cnt)
    t=t-1
