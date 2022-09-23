import sys

T=int(sys.stdin.readline())

for i in range(T):
    N, M = map(int,sys.stdin.readline().split())
    num=list(map(int,sys.stdin.readline().split()))
    a=[0 for j in range(N)]
    a[M]=1
    
    count =0
    
    while True:
        if num[0]==max(num):
            count+=1
            if a[0]==1:
                print(count)
                break
            else:
                num.pop(0)
                a.pop(0)
        else:
            num.append(num.pop(0))
            a.append(a.pop(0))
            
            