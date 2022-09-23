import sys
n=int(sys.stdin.readline())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    L=list(map(int,input().split()))
    M=[[L[i],0] for i in range(a)]
    M[b][1]=1
    count=0
    k=0
    N=[]
    for i in range(1,10):
        c=0
        for j in range(a):
            if L[j]==i:
                c+=1
        N.append(c)
    for i in range(9,0,-1):
        while N[i-1]>0:
            for j in range(a):
                if M[j][0]==i:
                    count+=1
                    if M[j][1]==1:
                        print(count)
                        N[i-1]=1
                        k=1
                    else:
                        if j==0:
                            del M[0]
                        elif j==a-1:
                            del M[j]
                        else:
                            M=M[j+1:]+M[:j]
                    N[i-1]=N[i-1]-1
                    break
        
        if k==1:
            break