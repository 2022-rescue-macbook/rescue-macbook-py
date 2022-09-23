from sys import stdin
n=int(stdin.readline())
for _ in range(n):
    c=0
    i=int(stdin.readline().split()[1])
    Q=list(map(int,stdin.readline().split()))
    sort=sorted(Q)
    while 1:
        if i==0:
            if Q[0]==sort[-1]:
                c+=1
                break
            else:
                Q.append(Q.pop(0))
                i=len(Q)
        elif Q[0]==sort[-1]:
            Q.pop(0)
            sort.pop()
            c+=1
        else:
            Q.append(Q.pop(0))
        i-=1
    print(c)