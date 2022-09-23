import sys

def printer(N,M,L):
    result=[]
    print_que=[0]*N
    print_que[M]=1
    while L!=[]:  
        i=0
        while i<len(L):
            a=L[0]
            if a<L[i]:
                L=L[1:]
                L.append(a)
                print_que.append(print_que[0])
                print_que=print_que[1:]
                i=0
                continue
            else:
                i+=1
        result.append(print_que[0])
        print_que=print_que[1:]
        L=L[1:]

    return result.index(1)+1

for i in range(int(sys.stdin.readline())):
    s1=str(sys.stdin.readline()).rstrip().split(" ")
    s1=list(map(int,s1))
    s2=str(sys.stdin.readline()).rstrip().split(" ")
    s2=list(map(int,s2))
    print(printer(s1[0],s1[1],s2))