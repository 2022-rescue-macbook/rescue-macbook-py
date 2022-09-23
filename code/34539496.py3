for i in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    a=1
    while True:
        if c[0]==max(c):
            if b==0:
                print(a)
                break
            else:
                a+=1
                c.pop(0)
                b-=1
        else:
            if b==0:
                b=len(c)-1
            else:
                b-=1
            c.append(c.pop(0))