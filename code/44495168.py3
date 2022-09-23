t = int(input())

res = []

for i in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    
    M = max(imp)
    start = 0
    l = len(imp)
    count = 1
    while True:
        if imp[start] != M:
            imp.append(imp[start])
            if start == m:
                m += l 
            start += 1
        else:
            if start == m:
                break
            M = max(imp[start+1:start+l])
            start += 1
            count += 1
            l -= 1
    
    res.append(count)

for i in res:
    print(i)