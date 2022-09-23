from sys import stdin as si
for _ in range(int(si.readline())):
    n,m = map(int,si.readline().split())
    queue=list(zip(list(map(int,si.readline().split())),list(range(n))))
    front=0
    cnt=[0]*10
    for x in queue:
        cnt[x[0]]+=1

    order=1
    check=False
    for i in range(9,0,-1):
        while cnt[i]>0:
            if queue[front][0]==i:
                if queue[front][1]==m:
                    check=True
                    break
                front+=1
                order+=1
                cnt[i]-=1
            else:
                queue.append(queue[front])
                front+=1        
        if check:
            break
    print(order)