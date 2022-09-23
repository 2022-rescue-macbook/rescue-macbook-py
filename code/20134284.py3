import sys

input = lambda: sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    cnt = 0
    N, M = map(int,input().split())
    L = list(map(int,input().split()))
    idx = M
    while 1:
        if max(L)==L[0]:
            if idx==0:
                L.pop(0)
                cnt+=1
                break
            else:
                L.pop(0)
                cnt += 1
                if idx>0:
                    idx-=1
                else:
                    idx=len(L)-1

        else:
            L.append(L.pop(0))

            if idx>0:
                idx-=1
            else:
                idx=len(L)-1


    print(cnt)