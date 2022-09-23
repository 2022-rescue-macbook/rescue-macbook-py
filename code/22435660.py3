n = int(input())
for i in range(n):
    N,M = map(int,input().split())
    
    A= list(map(int,input().split()))
    B=list(set(A))
    
    A=[[i,0] for i in A]
    A[M][1] = 1

    C=[]

    while B:
        temp = [i for i, value in enumerate(A) if value[0] == max(B)]
        
        for i in A: 
            if i[0] == max(B):
                C.append(i)
                
        A=A[max(temp):]+A[:max(temp)] 
       
        A=[i for i in A if i[0] !=max(B)] 

        B.remove(max(B))
     
    for i in C:
        if i[1]==1:
            print(C.index(i)+1)
            break