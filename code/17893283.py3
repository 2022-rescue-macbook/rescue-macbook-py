t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    plist=list(map(int,input().split()))
    queue=[i for i in range(n)]
    
    prinum=[]
    for doc in plist:
        prinum.append(doc)
    
    result=[0 for x in range(n)]
    
    seq=1
    while queue:
        if plist[queue[0]]==max(prinum):
            prinum.remove(max(prinum))
            result[queue.pop(0)]=seq
            seq+=1
        else:
            queue.append(queue.pop(0))
    print(result[m])
    