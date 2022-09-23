for _ in range(int(input())):
    N,M=map(int,input().split())
    l=list(map(int,input().split()))
    r=1
    while l:
        if l[0]==max(l):
            del l[0]
            if M==0:
                print(r)
                break
            r+=1
            M-=1
            continue
        if M==0:
            M+=len(l)-1
        else:
            M-=1
        l.append(l.pop(0))