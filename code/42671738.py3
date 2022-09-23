import sys
n=int(input())
result=[]
def queue(N,M,ip):
    queue=[]
    result=1
    for i in range(N):
        queue.append(ip[i])
    while True:
        temp=1
        current_ip=queue[0] # 1
        for i in range(1,len(queue)): # 1,2,3
            if queue[i]>current_ip: # 2 > 1
                queue.pop(0)
                queue.append(current_ip)
                if M!=0:
                    M-=1
                elif M==0:
                    M=len(queue)-1
                temp=0
                break
            else:
                continue
        if temp==1:
            if M==0:
                return result
            result+=1
            queue.pop(0)
            M-=1
for i in range(n):
    N, M = map(int,sys.stdin.readline().split())
    ip=list(map(int,sys.stdin.readline().split()))
    result.append(queue(N,M,ip))
for i in result:
    print(i)