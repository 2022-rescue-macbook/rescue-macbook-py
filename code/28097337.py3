test_case=int(input())

for _ in range(test_case):
    N,M=map(int,input().split())
    document=list(map(int,input().split()))
    count=0
    check=[0 for _ in range(N)]
    check[M]=1
    while True:
        if document[0]==max(document):
            count+=1
            if check[0]!=1:
                document.pop(0)
                check.pop(0)
            else:
                print(count)
                break
        else:
            document.append(document[0])
            check.append(check[0])
            document.pop(0)
            check.pop(0)
        
        
