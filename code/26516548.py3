N = int(input())
result = []
for i in range(N):
    C,K = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    while arr:
        bchcek = False
        for i in range(1,len(arr)):
            if arr[0] < arr[i]:
                arr.append(arr.pop(0))
                bchcek = True
                if K == 0:
                    K = len(arr)-1
                else:
                    K-=1
                break
                
        if bchcek == False:
            arr.pop(0)
            cnt +=1
            if (K == 0):
                result.append(cnt)
                break
            else:
                K-=1
            
for i in result:
    print(i)