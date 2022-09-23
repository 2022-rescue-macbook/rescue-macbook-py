import math
import sys

def Is_Max(N):
    try:
        if max(N[1:])>N[0]:
            return 1
    except:
        return 0
    
queue=[]
pos=0
T=int(sys.stdin.readline())

for i in range(T):
    N,M=map(int, sys.stdin.readline().split())
    queue=list(map(int,sys.stdin.readline().split()))
    pos=M
    
    while queue!=[]:
        if Is_Max(queue)==1:
            temp=queue.pop(0)
            queue.append(temp)
            pos-=1
            if pos<0:
                pos+=len(queue)
        else:
            if pos==0:
                print(N-len(queue)+1)
                break
            else:
                pos-=1
            queue.pop(0)