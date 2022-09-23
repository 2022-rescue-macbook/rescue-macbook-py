import sys

num=int(sys.stdin.readline().rstrip())

for _ in range(num):
    n,m=map(int,sys.stdin.readline().rstrip().split())

    pl=list(map(int,sys.stdin.readline().rstrip().split()))
    cl=[0 for i in range(n)]
    cl[m]=1

    cnt=0
    while 1:
        if pl[0] ==max(pl):
            cnt+=1

            if cl[0]!=1:
                del pl[0]
                del cl[0]
            else:
                print(cnt)
                break

        else:
            pl.append(pl[0])
            cl.append(cl[0])
            del pl[0]
            del cl[0]