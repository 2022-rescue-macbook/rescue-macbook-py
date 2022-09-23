for _ in range(int(input())):
    n,target = map(int,input().split())
    d = {i:k for i,k in enumerate(map(int,input().split()))}
    a = list(range(n)) 
    front = 0
    count = 0
    b = -1
    while b!=target:
        front%=len(a)
        m = max(d.values())
        while d[a[front]] != m:
            front = (front+1)%len(a)
        del d[a[front]]
        b = a.pop(front)
        count += 1
    print(count)