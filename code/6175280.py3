import sys
read = lambda : sys.stdin.readline().replace('\n', '')

num = int(read())
for i in range(num):
    n, m = map(int, read().split())
    arr = list(map(int, read().split()))
    pq = []
    order = 0
    
    for i in range(len(arr)):
        pq.append({"priority":arr[i], "index":i})
    
    while True:
        a = pq.pop(0)
        top = True
        for p in pq:
            if p["priority"] > a["priority"]:
                top = False
                break
        if top == False:
            pq.append(a)
        else:
            order += 1
            if a["index"] == m:
                break
    print(order)
   