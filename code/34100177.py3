import sys

T=int(sys.stdin.readline())
for i in range(T):
    N,M=map(int,sys.stdin.readline().split())
    doc=list(map(int,sys.stdin.readline().split()))
    doc2=[]
    cnt=0
    for i in range(N):
        doc2.append([i,doc[i]])
    tmp=doc2[M]
    while True:
        flag=True
        check=max(doc)
        while True:
            if(doc2[0]==tmp and check==tmp[1]):
                flag=False
                cnt+=1
                break
            
            elif(doc2[0][1]==check):
                doc2.pop(0)
                doc.remove(check)
                cnt+=1
                break
            else:
                doc2.append(doc2.pop(0))
        if(flag==False):
            print(cnt)
            break