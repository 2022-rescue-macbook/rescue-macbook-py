import sys
case = int(sys.stdin.readline())
for _ in range(case) :
    ea, target = map(int, sys.stdin.readline().rstrip().split())
    importance = list(map(int, sys.stdin.readline().rstrip().split())) 
    que = [*enumerate(importance)]
    cnt = 0
    while True :
        mx = max(importance)
        if que[0][1] == mx :
            cnt += 1

            if que[0][0] == target :
                print(cnt)
                break
            else :
                que.pop(0)
                importance.pop(0) 
        else :
            que.append(que.pop(0))
            importance.append(importance.pop(0))
