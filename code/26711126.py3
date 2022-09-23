import sys
t=int(sys.stdin.readline())
for i in range(t):
    n, m=map(int, sys.stdin.readline().split())
    l=list(map(int, sys.stdin.readline().split()))
    ped=0
    while 1:
        if m==0 and l[0]==max(l):
            print(ped+1)
            break
        elif m==0 and l[0]!=max(l):
            l.append(l[0])
            del l[0]
            m=len(l)-1
        elif l[0]==max(l):
            del l[0]
            ped+=1
            m-=1
        else:
            l.append(l[0])
            del l[0]
            m-=1

