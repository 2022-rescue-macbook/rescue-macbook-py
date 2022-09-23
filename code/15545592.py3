import sys
for i in range(int(sys.stdin.readline())):
    size,idx=map(int,sys.stdin.readline().split())
    que=list(map(int,sys.stdin.readline().split()))
    idx_li=[0 for i in range(size)]
    idx_li[idx]=1
    cnt=0
    while 1:
        if que[0]==max(que):
            cnt+=1
            if idx_li[0]==1:
                print(cnt)
                break
            else:
                que.pop(0)
                idx_li.pop(0)
        else:
            que.append(que.pop(0))
            idx_li.append(idx_li.pop(0))