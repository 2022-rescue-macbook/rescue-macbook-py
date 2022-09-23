import sys
t=int(sys.stdin.readline().rstrip())
for i in range(t):
    n,m=list(map(int,sys.stdin.readline().split(" ")))
    a=list(map(int,sys.stdin.readline().split(" ")))
    b=list(range(len(a)))
    target=b[m]

    cnt=0

    while True:
        if a[0]==max(a):
            cnt=cnt+1
            if b[0]==target:
                print(cnt)
                break
            else:
                a.pop(0)
                b.pop(0)
        else:
            a.append(a.pop(0))
            b.append(b.pop(0))