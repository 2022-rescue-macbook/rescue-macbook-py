import sys
for i in range(int(sys.stdin.readline())):
    A,B = map(int,sys.stdin.readline().split())
    C = list(map(int,sys.stdin.readline().split()))
    D =[]
    num = 0
    for i in range(A):
        D.append((C[i],i))
    
    while True:
        num+=1
        while D[0][0] != max(C):
            D.append(D.pop(0))
        C.remove(max(C))
        if D.pop(0)[1] == B:
            print(num)
            break