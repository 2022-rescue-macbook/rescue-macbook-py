for i in range(int(input())):
    cnt = 0
    queue = []
    N, point = map(int,input().split())
    lists = list(map(int,input().split()))
    for i in range(N):
        queue.append((i,lists[i]))
    while True:
        flag = True
        temp=queue[0][1]
        for i in range(len(queue)):
            if queue[i][1] > temp:
                flag = False
                break
        if flag:
            k = queue.pop(0)
            cnt +=1
            if k[0] == point:
                print(cnt)
                break
        else:
            k = queue.pop(0)
            queue.append(k)

