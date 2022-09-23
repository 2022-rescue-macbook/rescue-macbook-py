import sys

A = int(sys.stdin.readline())
result = []
for i in range(A):
    n,m = map(int, sys.stdin.readline().split())
    k = list(map(int,sys.stdin.readline().split()))
   
    a = 1
    if n ==1:
        result.append(a)
    else :
        for i in range(n):
            if m == k.index(max(k)):
                result.append(a)
                break
            else :
                for i in range(k.index(max(k))+1):
                    k.append(k[0])
                    k.pop(0)
                    if m == 0:
                        m = len(k)-1
                    else :
                        m -=1
                k.pop()
                a += 1
            
for i in result:
    print(i)