#프린터 큐(실버3)
import sys
t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int, sys.stdin.readline().split())
    importance=list(map(int,sys.stdin.readline().split()))
    order=1
    temp=[0]*len(importance)
    temp[m]='target'

    while True:
        if importance[0]<max(importance):
            importance.append(importance.pop(0))
            temp.append(temp.pop(0))
        elif temp[0]=='target':
            print(order)
            break
        else:
            order=order+1
            importance.pop(0)
            temp.pop(0)
            