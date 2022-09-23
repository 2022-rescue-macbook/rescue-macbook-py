for _ in range(int(input())):
    N, M=map(int, input().split())
    a=list(map(int, input().split()))
    b=1
    while True:
        c=a.index(max(a))
        if M==c:
            print(b)
            break
        else:
            a+=a[:c]
            del a[:c+1]
            M+=(int(M<c)*N-c-1)
            N-=1
            b+=1