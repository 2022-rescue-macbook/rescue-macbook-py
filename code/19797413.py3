t = int(input())
while t:
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    cnt=1
    while True:
        if q.index(max(q)) == 0:
            if m==0:
                break
            else:
                del q[0]
                m-=1
                cnt+=1
        else:
            temp = q[0]
            del q[0]
            q.append(temp)
            if m==0:
                m=len(q)-1
            else:
                m-=1
    print(cnt)
    t-=1