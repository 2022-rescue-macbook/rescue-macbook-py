T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    queue=[i for i in range(N)]
    importance=list(map(int,input().split()))
    count=0
    while True:
        if importance[0]<max(importance):
            queue.append(queue[0])
            importance.append(importance[0])
            del queue[0]
            del importance[0]
        else:
            if queue[0]==M:
                count+=1
                print(count)
                break
            else:
                del queue[0]
                del importance[0]
                count+=1