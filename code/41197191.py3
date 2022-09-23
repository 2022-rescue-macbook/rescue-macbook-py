import sys
input = sys.stdin.readline
T= int(input())
for _ in range(T):
    n,m = map(int,input().split())
    imp =list(map(int,input().split()))
    idx =list(range(len(imp)))
    target=[]
    target.append(idx[m])
    order=0
    while 1:
        if imp[0]==max(imp):
            order+=1
            if idx[0]==target[0]:
                print(order)
                break
            else:
                idx.pop(0)
                imp.pop(0)
        else:
            idx.append(idx.pop(0))
            imp.append(imp.pop(0))
            
    