from _collections import deque
T=int(input())
res=[]
for _ in range(T):
    num,loc=map(int,input().split())
    score=[(key,value)for key,value in enumerate(list(map(int,input().split())))]
    Q=deque(score)
    cnt=0
    while True:
        num1=Q.popleft()
        if any(num1[1]<x[1]for x in Q):
            Q.append(num1)
        else:
            cnt+=1
            if num1[0]==loc:
                res.append(cnt)
                break
for y in res:
    print(y)
