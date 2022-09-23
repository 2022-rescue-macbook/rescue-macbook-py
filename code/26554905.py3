for _ in range(int(input())):
    count = 0
    n,crr = map(int,input().split())
    que = list(map(int,input().split()))
    while crr > -1:
        while crr:
            if que[0] < max(que):
                que.append(que[0])
            else:
                count += 1
            del que[:1]
            crr -= 1
        if que[crr] < max(que):
            que.append(que[crr])
            del que[:1]
            crr = len(que)-1
        else:
            count += 1
            crr -= 1
    print(count)