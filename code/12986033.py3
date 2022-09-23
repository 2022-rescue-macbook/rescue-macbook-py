for x in range(int(input())):
    m,n=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(range(m))
    cnt=0
    while True:
        b=B.pop(0)
        if max(A) == A[0]:
            A.pop(0)
            cnt+=1
            if b==n:
                print(cnt)
                break
        else:
            A.append(A.pop(0))
            B.append(b)