num_case=int(input())
result=[]
for i in range(num_case):
    n,m=map(int,input().split())
    q = list(map(int,input().split()))
    count=0
    # mx=max(q)
    while n>0:
        mx=max(q)
        if q[0] < mx:
            q.append(q.pop(0))
            m-=1
            if m<0:
                m=n-1
        else:
            q.pop(0)
            n -= 1
            m -= 1
            count += 1
            if m < 0:
                break
    result.append(count)
for i in result:
    print(i)
