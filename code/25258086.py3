t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    idx = [j for j in range(n)]
    count = 1
    while(True) :
        if q[0] != max(q) :
            q.append(q[0])
            del q[0]
            idx.append(idx[0])
            del idx[0]
        else :
            if(idx[0] == m) :
                print(count)
                break
            else :
                del q[0]
                del idx[0]
            count += 1