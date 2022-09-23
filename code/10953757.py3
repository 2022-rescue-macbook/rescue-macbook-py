T=int(input())
for i in range(T):
    queue=[]
    cnt=0
    N,M=map(int,input().split())
    queue=input().split()
    ans=[0]*N
    ans[M]=1
    while(True):
        if queue.index(max(queue)) == 0:
            del queue[0]
            cnt += 1
            if ans[0] == 1:
                print(cnt)
                break
            else:
                del ans[0]

        else:
            queue.append(queue[0])
            del queue[0]
            ans.append(ans[0])
            del ans[0]
