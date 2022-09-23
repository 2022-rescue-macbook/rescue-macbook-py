import sys
input=sys.stdin.readline
x=int(input())

for i in range(x):
        se=[]
        n,m=map(int,input().split())
        b=list(map(int,input().split()))
        t=b[m]
        b.insert(m+1,-1)

        sum1=0

        while True:
 
                if b[0]==max(b) and b[0]>0:
                
                    sum1+=1

                        
                    if b[0]==t and b[1]==-1:
                        
                        
                        print(sum1)

                        break
                    b.pop(0)
                
                                

                else:

                
                    s=b.pop(0)
                    b.append(s)
