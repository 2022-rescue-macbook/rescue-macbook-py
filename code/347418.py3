for T in range(int(input())):
    n,m=map(int,input().split())
    a= list(map(int,input().split()))
    b=[[i,a[i]]for i in range(n)]
    a.sort()
    a.reverse()
    index=0
    cnt=1

    for number in a:
        while 1:
            if b[index][1]==number:
                break
            index=(index+1)%n
        if b[index][0]==m:
            print(cnt)
            break
        cnt+=1
        index=(index+1)%n

