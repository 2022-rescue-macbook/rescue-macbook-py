# 프린터 큐

import sys
for _ in range(int(input())) :
    N, M = map(int,sys.stdin.readline().split())
    que = list(map(int,sys.stdin.readline().split()))
    idx = list(range(len(que))) # 순서 저장
    idx[M] = 'target'

    pop_num = 0
    ans = 0
    while (True) :
        if que[0] == max(que) :
            ans += 1
            if idx[0] == "target" :
                print(ans)
                break

            else :
                que.pop(0)
                idx.pop(0)
        else :
            que.append(que.pop(0))
            idx.append(idx.pop(0))