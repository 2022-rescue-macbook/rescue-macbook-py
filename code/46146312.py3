nn = int(input())
result = []
for i in range(nn):
    ms, qmn = map(int,input().split())
    q = list(map(int,input().split()))
    fl = len(q)
    p = qmn
    a = 'F'
    while a=='F':
        m = max(q)
        while q[0]!=m:
            q.append(q.pop(0))
            if p>0:
                p=p-1
            else:
                p=len(q)-1
        if p==0:
            result.append(fl-len(q)+1)
            a='T'
            break
        q.pop(0)
        if p>0:
            p=p-1
        else:
            p=len(q)-1
for i in range(nn):
    print(result[i])