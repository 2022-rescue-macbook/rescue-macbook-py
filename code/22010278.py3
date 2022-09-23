import sys
s = sys.stdin.readline
for _ in range(int(s())):
    n, m = map(int, s().split())
    pos = list(range(n))
    que = list(map(int, s().split()))
    
    cnt = 0

    while True:
        if que[0] != max(que):
            que.append(que.pop(0))
            pos.append(pos.pop(0))
        elif pos[0] == m:
            print(cnt + 1)
            break
        else:
            que.pop(0)
            pos.pop(0)
            cnt += 1