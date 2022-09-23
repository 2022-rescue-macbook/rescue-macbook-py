import sys


case=int(sys.stdin.readline().rstrip())
for i in range(case):
    N, idx = list(map(int,sys.stdin.readline().rstrip().split()))
    q = list(map(int,sys.stdin.readline().rstrip().split()))
    start=0
    result=1
    Min=min(q)
    while True:
        if max(q)>q[idx]:
            start=q.index(max(q))
            q[start]=Min-1
            result+=1
            q=q[start:]+q[:start]
            idx+=N-start
            if idx>=N:
                idx-=N
        elif max(q)==q[idx]:
            for i in range(idx):
                k=i
                if k>=N:
                    k-=N
                if q[k]==q[idx]:
                    result+=1
            break
    print(result)    
        