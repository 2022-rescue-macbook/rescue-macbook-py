test=int(input())
for i in range(test):
    N,M=map(int,input().split())       #N=수, M=알고자 하는 문서의 위치
    imp=list(map(int,input().split())) #중요도
    cnt=0
    while True:
        if imp[0]<max(imp):
            a=imp.pop(0)
            imp.append(a)
            if M==0:
                M=N-1
            else:
                M-=1
            continue
        elif imp[0]==max(imp):
            del imp[0]
            cnt+=1
            N-=1
            if M==0:
                break
            else:
                M-=1
        if not imp:
            break
    print(cnt)
        
