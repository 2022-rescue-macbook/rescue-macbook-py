import sys
input=sys.stdin.readline
c=int(input())

for _ in range(0,c):
    N, M = list(map(int, input().split()))
    l = list(map(int, input().split()))

    m=M
    i=1

    if N == 1:
        print(1)
        continue
    
    while l:
        if l[0] == max(l):
            if m == 0:
                print(i)
                break
            m-=1
            i+=1
            l.pop(0)
            
        else:
            if m == 0:
                m=len(l)-1
            else: m-=1
            l.append(l.pop(0))

        
