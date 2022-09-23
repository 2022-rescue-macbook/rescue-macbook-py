n = int(input())

for i in range(n):
    M,N = map(int,input().split())
    idx = [i for i in range(M)]
    q = list(map(int,input().split()))
    cnt=1
    while q:
        if max(q)!=q[0]:
            q.append(q.pop(0))
            idx.append(idx.pop(0))
            continue
        q.pop(0)
        if idx.pop(0)==N:
            break
        cnt+=1
    print(cnt)




