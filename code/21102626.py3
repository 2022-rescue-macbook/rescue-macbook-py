tc = int(input())

for t in range(tc):
    n, pos = map(int, input().split())
    count = 0
    q = list(map(int, input().split()))
    m = max(q)
    while q:
        if q[0] == m and pos == 0:
            count += 1
            q.pop(0)
            break
            
        elif q[0] == m:
            q.pop(0)
            m = max(q)
            count += 1

        else:
            q.append(q.pop(0))
            
        if pos == 0:
            pos = len(q) - 1
        else:
            pos -= 1
    
    print(count)