import sys
T=int(input())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    queue=list(map(int,sys.stdin.readline().split()))
    a=0
    n=0
    while True:
        if queue[a]!=max(queue[a:]):
            if a==M:
                M+=len(queue[a:])
            queue.append(queue[a])
            a+=1
        else:
            n+=1
            if a==M:
                break
            a+=1
    print(n)