tc=int(input())
count=0

for i in range(tc):
    n, m=map(int, input().split())
    que=list(map(int, input().split()))
    count=0
    imp=que[m]
    po=0
    while len(que)>0:
        if m==0 and que[0]!=max(que):
            que.append(que.pop(0))
            m=len(que)-1
        elif m==0 and que[0]==max(que):
            count+=1
            break
        elif que[0]==max(que):
            po=que.pop(0)
            count+=1
            m-=1           
        else:
            que.append(que.pop(0))
            m-=1
       
    print(count)
