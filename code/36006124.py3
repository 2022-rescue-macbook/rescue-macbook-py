import sys
t = int(input())
for k in range(t):
    n,m = map(int,sys.stdin.readline().strip().split(" "))
    d = {}
    l = list(map(int,sys.stdin.readline().strip().split(" ")))
    l2 = []
    for i in range(len(l)):
        d[i] = l[i]
        l2.append(i)
  
    c = 0
    a = 0
    while(1):
        if d[l2[0]] == max(d.values()):
            
            if l2[0] == m: 
                a = a+1
                c =1
                
            else:
                del d[l2[0]]
                del l2[0]
                a = a+1
        else:
            s = l2[0]
            del l2[0]
            l2.append(s)
        if c == 1:
            break
                

    print(a)