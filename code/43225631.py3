c=int(input())
for i in range(c):
    cnt=0 
    fir=list(map(int,input().split()))
    sec=list(map(int,input().split()))
    M=max(sec)
    while(True):
        if fir[1]==0:
            if sec[0]<M:
                sec.append(sec[0])
                sec.pop(0)
                fir[1]=len(sec)-1
            else:
                cnt+=1
                print(cnt)
                break
        elif sec[0]<M:
            sec.append(sec[0])
            sec.pop(0)
            fir[1]-=1 
        else:
            cnt+=1
            sec.pop(0)
            M=max(sec)
            fir[1]-=1