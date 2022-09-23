import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,M=map(int, input().split())
    priority=list(map(int, input().split()))
    docLocation=[0 for _ in range(N)]
    docLocation[M]=1
    cnt=0
    while True:
        if priority[0]==max(priority):
            cnt+=1
            if docLocation[0]==1:
                print(cnt)
                break
            else:
                del priority[0]
                del docLocation[0]
        else:
            priority.append(priority[0])
            docLocation.append(docLocation[0])
            del priority[0]
            del docLocation[0]