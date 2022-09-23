T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    document = list(map(int,input().split()))
    max_=max(document)
    fin_=False
    time=0
    while fin_==False: 
        if M==0:
            if document[0]>=max_:
                time+=1
                fin_=True
                break
            else:
                M=len(document)-1
                document.append(document[0])
                del document[0]
        else:
            if document[0]>=max_:
                del document[0]
                M-=1
                time+=1
                max_=max(document)
            else:
                M-=1
                document.append(document[0])
                del document[0]
            
    
        
    print(time)