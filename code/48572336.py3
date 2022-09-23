case=int(input())
for _ in range(case):
    n,m=map(int,input().split())
    q=list(map(int,input().split()))
    s=list(reversed(sorted(q)))
    cnt,i=0,0
    while True:
        if q[i]==s[cnt]:
            cnt+=1
            if i==m:
                break
            q[i]=-1
        i=(i+1)%n
    print(cnt)